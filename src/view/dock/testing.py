from PyQt4 import QtGui, QtCore

class Testing(QtGui.QDockWidget):
    
    def __init__(self):
        super(Testing, self).__init__()
        self.widget = QtGui.QWidget()
        