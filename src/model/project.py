'''
:Description:
    Module that contains the model of a Project:
        - a collection of files, resources and configurations
        
:Depends:
    - python yaml plugin (optional)
    If yaml is not found, project str() returns the project name.
        
'''
from PyQt4 import QtGui

class Project:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Project, self).__new__(
                self, *args, **kwargs)
            self.projects = QtGui.QStandardItemModel() # Project data
            self.projects.setHorizontalHeaderItem(0, 
                                                  QtGui.QStandardItem("Project Name"))
        return self._instance