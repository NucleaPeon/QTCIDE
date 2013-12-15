'''
TODO: 
    - Validate that name is unique upon 
        a) rename of project
        b) new project
        
'''
from PyQt4 import QtGui, QtCore
import view.menu.projectcontext
import view.window


class Project:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Project, self).__new__(
                self, *args, **kwargs)
            self.projects = QtGui.QStandardItemModel() # Project data
            self.projects.setHorizontalHeaderItem(0, 
                                                  QtGui.QStandardItem("Project Name"))
            self.projecttree = QtGui.QTreeView()
            self.projectcontextmenu = view.menu.projectcontext.ProjectContextMenu()
            self.projectcache = {}
        return self._instance
    
    def addNewProject(self, project_name):
        if not project_name:
            return
        
        if not self.projectcache.get(project_name, None) is None:
            print("TODO: Project already exists by that name")
            return
        
        proj = QtGui.QStandardItem(project_name)    
        self.projects.appendRow(proj)
        self.projectcache[project_name] = proj
        # Select the project in the treeview is none is previously selected
        if self.projects.rowCount() == 1:
            qmindex = self.projects.index(0, 0)
            self.projecttree.setCurrentIndex(qmindex)
        return proj