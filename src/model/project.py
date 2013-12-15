'''
:Description:
    Module that contains the model of a Project:
        - a collection of files, resources and configurations
        
:Depends:
    - python yaml plugin (optional)
    If yaml is not found, project str() returns the project name.
        
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
        return self._instance
    
    def addNewProject(self, project_name):
        print("Adding {}".format(project_name))