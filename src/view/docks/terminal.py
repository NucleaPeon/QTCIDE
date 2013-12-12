'''
'''
from PyQt4 import QtGui, QtCore

'''
:Description:
    Terminal that takes inputs and presents information
    regarding IDE-specifics 
'''
class TerminalDock(QtGui.QWidget):

    __version__ = "v 0.10"
    
    def __init__(self, *args, **kwargs):
        '''
        '''
        super(TerminalDock, self).__init__()
        self.setMinimumHeight(100)
        vbox = QtGui.QVBoxLayout()
        width = kwargs.get('width', self.width())
        self.terminalinput = QtGui.QLineEdit()
        self.setLayout(vbox)
        scrollarea = QtGui.QScrollArea()
        scrollarea.resize(width, 100)
        self.textedit = QtGui.QTextEdit()
        pal = self.textedit.palette()
        pal.setColor(QtGui.QPalette.Base, QtCore.Qt.black)
        self.textedit.setPalette(pal)
        self.connect(self.textedit,
            QtCore.SIGNAL("keyPressEvent(const QKeyEvent &)"),
            self.keyPressEvent)
        self.textedit.setTextColor(QtGui.QColor(QtCore.Qt.white))
        self.textedit.resize(width - 24, 100 - 24)
        self.textedit.setReadOnly(True)
        self.textedit.setText(
            "> QTCIDE [{}]".format(self.__version__))
        self.consolefont = QtGui.QFont()
        self.consolefont.setStyleHint(QtGui.QFont.Monospace)
        self.textedit.setCurrentFont(self.consolefont)
        
        scrollarea.setWidget(self.textedit)
        vbox.addWidget(scrollarea)
        vbox.addWidget(self.terminalinput)
        scrollarea.adjustSize()

    @QtCore.pyqtSlot(QtGui.QKeyEvent)
    def keyPressEvent(self, e):
        if self.terminalinput.text() == "":
            return
        if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:
            self.textedit.append("> {}".format(self.terminalinput.text()))
            self.terminalinput.clear()
