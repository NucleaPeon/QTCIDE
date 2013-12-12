from PyQt4 import QtGui, QtCore

class Project(QtGui.QDockWidget):
    
    def __init__(self):
        super(Project, self).__init__()
        self.widget = QtGui.QWidget()
        