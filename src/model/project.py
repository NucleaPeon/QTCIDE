'''
Project Model

:Description:
    This project model is not a barebones model. It contains all the
    functionality for handling projects and data is saved in the
    cache

TODO: 
    - Validate that name is unique upon 
        a) rename of project
        b) new project
        
'''
from PyQt4 import QtGui, QtCore
import view.menu.projectcontext
import view.window
import controller.project
import model.data.project as data

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
    
    def addNewProject(self, project_name, project_icon=None):
        if not project_name:
            return
        
        if not self.projectcache.get(project_name, None) is None:
            print("TODO: Project already exists by that name")
            return
        
        if not project_icon is None:
            proj = QtGui.QStandardItem(project_icon, project_name)
        else:
            proj = QtGui.QStandardItem(project_name)    
        self.projects.appendRow(proj)
        self.projects.sort(0)
        self.projectcache[project_name] = data.ProjectData(proj)
        # Select the project in the treeview is none is previously selected
        if self.projects.rowCount() == 1:
            qmindex = self.projects.index(0, 0)
            self.projecttree.setCurrentIndex(qmindex)
        view.actions.project.close.CloseProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        return proj
    
    def closeProject(self):
        selected = self.projecttree.currentIndex().row()
        text = self._get_project_name()
        if text in self.projectcache.keys():
            del self.projectcache[text]
        self.projects.removeRow(selected)
        view.actions.project.close.CloseProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        
    def saveProject(self, project_name=None):
        '''
        :Description:
            Makes a request to the controller to persist the specified
            project; project_name defaults to the current selected project.
        
        :Parameters:
            - project_name: grabs the text from currently selected project
            
        '''
        if project_name is None:
            project_name = self._get_project_name()
        controller.project.saveProject(self.projectcache[project_name].qsi_proj)
        
    def _get_project_name(self):
        '''
        :Description:
            Returns the text of the selected project from the model
            
        :Returns:
            String of the selected project name
        '''
        return self.projects.item(self.projecttree.currentIndex().row()).text()