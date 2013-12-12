from PyQt4 import QtGui, QtCore
import os

class Project(QtGui.QDockWidget):
    
    def __init__(self):
        super(Project, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join('res', 'folder-development.png'))
