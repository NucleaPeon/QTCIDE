from PyQt4 import QtGui, QtCore
import os

class Project(QtGui.QDockWidget):
    
    def __init__(self):
        super(Project, self).__init__()
        # Set up dock
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join('res', 
                                             'folder-development.png'))
        # Connect Custom Menu creation TODO
        # Initialize Model which is saved here
        self.projects = QtGui.QStandardItemModel()
        
        # Initialize TreeView for model to sit in
        self.projecttree = QtGui.QTreeView()
        self.projecttree.setModel(self.projects)
        self.projects.setHorizontalHeaderItem(0, 
                                              QtGui.QStandardItem("Project Name"))
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.projecttree)