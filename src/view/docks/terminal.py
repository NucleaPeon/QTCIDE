'''
'''
from PyQt4 import QtGui, QtCore

class TerminalDock(QtGui.QWidget):
    
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
        self.textedit.setTextColor(QtGui.QColor(QtCore.Qt.white))
        self.textedit.resize(width - 24, 100 - 24)
        self.textedit.setReadOnly(True)
        self.textedit.setText("Terminal Loaded: QTCIDE [V 0.10]")
        self.consolefont = QtGui.QFont()
        self.consolefont.setStyleHint(QtGui.QFont.Monospace)
        self.textedit.setCurrentFont(self.consolefont)
        
        scrollarea.setWidget(self.textedit)
        vbox.addWidget(scrollarea)
        vbox.addWidget(self.terminalinput)
        scrollarea.adjustSize()