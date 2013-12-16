from PyQt4 import QtGui, QtCore
import model.project
import view.menu.projectcontext
import controller.project
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
        self.icon = QtGui.QIcon(os.path.join('res', 
                                             'folder-development.png'))
        # Initialize TreeView for model to sit in
        self.projecttree = model.project.Project().projecttree
        self.projecttree.setModel(model.project.Project().projects)
        self.projecttree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.projecttree)
        self.connect(self.projecttree,
                QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
                self.__project_context)
        
        
    def __project_context(self):
        view.menu.projectcontext.ProjectContextMenu().displayProjectMenu()
        print("Called when different project is selected, run context validation")