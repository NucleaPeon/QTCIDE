from PyQt4 import QtGui, QtCore
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.project
import view.components.project
import controller.project
import os

class Project(QtGui.QDockWidget):

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__()
        self.widget = QtGui.QWidget()
        # Set up dock
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'folder-development.png'))
        # Initialize TreeView for model to sit in
        
        self.project = view.components.project.Project(menu = kwargs.get('menu'))
        
        self.project.projecttree.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.project.projecttree)
        
        