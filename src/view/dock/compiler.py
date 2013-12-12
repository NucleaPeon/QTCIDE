from PyQt4 import QtGui, QtCore

class Compiler(QtGui.QDockWidget):
    
    def __init__(self):
        super(Compiler, self).__init__()
        self.widget = QtGui.QWidget()
        