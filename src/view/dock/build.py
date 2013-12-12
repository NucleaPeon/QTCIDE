from PyQt4 import QtGui, QtCore

class Build(QtGui.QDockWidget):
    
    def __init__(self):
        super(Build, self).__init__()
        self.widget = QtGui.QWidget()
        