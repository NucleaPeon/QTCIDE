from PyQt4 import QtGui, QtCore

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
        self.textedit.setText("")
        # Add Widgets to Layout
        self.scrollarea.setWidget(self.textedit)
        self.vbox.addWidget(self.scrollarea)
        self.vbox.addWidget(self.commandarea)
        # Connect slots
        self.connect(self.textedit,
                     QtCore.SIGNAL("keyPressEvent(const QKeyEvent &)"),
                     self.keyPressEvent)
        
    @QtCore.pyqtSlot(QtGui.QKeyEvent)    
    def keyPressEvent(self, e):
        if self.commandarea.text() == "":
            return
        if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:
            self.textedit.append(": {}".format(self.commandarea.text()))
            self.commandarea.clear()
        elif e.key() == QtCore.Qt.Key_Escape:
            self.commandarea.clear() # Easy way to clear the edit field