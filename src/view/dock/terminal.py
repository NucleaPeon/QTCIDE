from PyQt4 import QtGui, QtCore
import view.modal.QtPopupConfirm
import view.modal.QtPopupTextInput

class Terminal(QtGui.QDockWidget):
    
    def __init__(self):
        super(Terminal, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.vbox = QtGui.QVBoxLayout()
        self.widget.setLayout(self.vbox)
        # Monospace Font
        self.consolefont = QtGui.QFont()
        self.consolefont.setStyleHint(QtGui.QFont.Monospace)
        # scroll area settings
        self.scrollarea = QtGui.QScrollArea()
        self.scrollarea.setWidgetResizable(True)
        # line edit settings
        self.commandarea = QtGui.QLineEdit()
        # terminal output area
        self.textedit = QtGui.QTextEdit()
        self.textedit.setCurrentFont(self.consolefont)
        self.textedit.setReadOnly(True)
        self.textedit.clear()
        # Add Widgets to Layout
        self.scrollarea.setWidget(self.textedit)
        self.vbox.addWidget(self.scrollarea)
        self.vbox.addWidget(self.commandarea)
        # Connect slots
        self.connect(self.textedit,
                     QtCore.SIGNAL("keyPressEvent(const QKeyEvent &)"),
                     self.keyPressEvent)
        """ RECOGNIZED_COMMANDS uses string : callable format """
        self.RECOGNIZED_COMMANDS = {
            'clear': self.textedit.clear,
            'QtPopupConfirm': lambda: view.modal.QtPopupConfirm.QtPopupConfirm('test', 'this is a test').exec_(),
            'QtPopupTextInput': lambda: view.modal.QtPopupTextInput.QtPopupTextInput('test', 'this is a test').exec_()
        }
        
    @QtCore.pyqtSlot(QtGui.QKeyEvent)    
    def keyPressEvent(self, e):
        if self.commandarea.text() == "":
            return
        if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:

            self.parseCommand(self.commandarea.text())
            self.commandarea.clear()
        elif e.key() == QtCore.Qt.Key_Escape:
            self.commandarea.clear() # Easy way to clear the edit field
            
            
    def parseCommand(self, string):
        '''
        :Description:
            Essentially a python code parser
            
            Contains one or two+ arguments, separated by a space.
            See self.RECOGNIZED_COMMANDS for a map of what is accepted and
            what that string calls when inputted into the terminal
            
        :Usage:
            - 1 argument: you are inputting a command that is recognized
              by the IDE. This can be something as simple as "clear", 
              which clears the entire text area of the terminal.
            - 2+ arguments: You want to run a python command from inside
              the IDE while modules are loaded. Format is this:
                - module (separated by periods, same as if you were importing)
                - method name
                - (optional) arguments. Currently only string arguments are 
                  supported. TODO
        '''
        length = len(string.split(" "))
        if length == 1:
            if string in self.RECOGNIZED_COMMANDS:
                self.textedit.append(": [{}]".format(self.commandarea.text()))
                self.RECOGNIZED_COMMANDS[string]()
            else:
                self.textedit.append("X [{}]".format(self.commandarea.text()))
        else:
            pass # import modules and stuff