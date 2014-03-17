from PyQt4 import QtGui, QtCore
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.project
import view.components.project
import controller.project
import importlib
import os

class Project(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Project, self).__new__(
                self, *args, **kwargs)
            self.widget = QtGui.QWidget()
        return self._instance
    
    def __init__(self):
        super(Project, self).__init__()
        # Set up dock
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'folder-development.png'))
        # Initialize TreeView for model to sit in
        project = importlib.import_module('cache').load('view.components.project.Project')
        project.projecttree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(project.projecttree)
        
        