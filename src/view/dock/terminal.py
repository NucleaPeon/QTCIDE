from PyQt4 import QtGui, QtCore

class Terminal(QtGui.QDockWidget):
    
    def __init__(self):
        super(Terminal, self).__init__()
        self.widget = QtGui.QWidget()
        