from PyQt4 import QtGui, QtCore
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.project
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
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'folder-development.png'))
        # Initialize TreeView for model to sit in
        self.projecttree = model.project.Project().projecttree
        self.projecttree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.projecttree)
        self.connect(self.projecttree,
                QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
                view.menu.context.project.ProjectContextMenu().displayProjectMenu)
        self.projecttree.connect(self.projecttree.selectionModel(),
                QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                self.__project_context)
        
        
    def __project_context(self, selected, deselected):
        # Check save boolean from model.data
        proj = model.project.Project()
        
        if not proj._get_project_name() is None:
            status = proj.projectcache[proj._get_project_name()].save
            action = view.actions.project.save.SaveProjectAction().qaction
            action.setEnabled(status)
        else:
            # force everything to be disabled, no projects in treeview
            view.actions.project.save.SaveProjectAction().qaction.setEnabled(False)
            view.actions.project.close.CloseProjectAction().qaction.setEnabled(False)
        
        
        