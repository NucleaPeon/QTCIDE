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
import view.menu.context.project
import view.modal.config.window
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
            self.projecttree.setModel(self.projects)
            self.projectcontextmenu = view.menu.context.project.ProjectContextMenu()
            self.projectcache = {}
        return self._instance
    
    def addNewProject(self, name, icon=None):
        if not name:
            return
        
        # Returns ProjectData object
        if not self.projectcache.get(name, None) is None:
            print("TODO: Project already exists by that name")
            return
        
        if not icon is None:
            proj = QtGui.QStandardItem(icon, name)
        else:
            proj = QtGui.QStandardItem(name)    
        self.projects.appendRow(proj)
        self.projects.sort(0)
        self.projectcache[name] = data.ProjectData(name=name,
                                                   icon=icon,
                                                   save=True)
        # Select the project in the treeview is none is previously selected
        if self.projects.rowCount() == 1:
            qmindex = self.projects.index(0, 0)
            self.projecttree.setCurrentIndex(qmindex)
        view.actions.project.close.CloseProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        # FIXME
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projectcache[self._get_name()].save)
        return proj
    
    def closeProject(self):
        selected = self.projecttree.currentIndex().row()
        text = self._get_name()
        if text in self.projectcache.keys():
            del self.projectcache[text]
        view.actions.project.close.CloseProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        self.projects.removeRow(selected)
        
    def saveProject(self, name=None):
        '''
        :Description:
            Makes a request to the controller to persist the specified
            project; name defaults to the current selected project.
        
        :Parameters:
            - name: grabs the text from currently selected project
            
        '''
        
        if name is None:
            name = self._get_name()
        controller.project.saveProject(self.projectcache[name].qsi_proj)
        self.projectcache[name].save = False
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projectcache[name].save)
        
    def configuration(self):
        view.modal.config.window.ProjectConfiguration().exec_()
        
        
    def _get_name(self):
        '''
        :Description:
            Returns the text of the selected project from the model
            
        :Returns:
            String of the selected project name or None if no rows exist
        '''
        if self.projecttree.currentIndex().row() >= 0:
            return self.projects.item(self.projecttree.currentIndex().row()).text()
