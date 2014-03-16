from PyQt4 import QtGui, QtCore

class Project(QtGui.QStandardItemModel):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Project, self).__new__(
                self, *args, **kwargs) # Project data
            cls.projecttree = QtGui.QTreeView()
            cls.projecttree.setModel(cls.projects)
        return self._instance
    
    def __init__(self):
        self.setHorizontalHeaderItem(0, 
                QtGui.QStandardItem("Project Name"))
        
    def addProject(self, project):
        '''
        Adds a project to the graphical view based on the model
        
        :Description:
            Checks project information, verifies, and adds project
            to the model/view ui representation.
            
            Verification includes:
                - proper name format
                - including icon in QStandardItem
        
        :Parameters:
            - project: model.project object which is placed into a
                       ProjectItem class and added.
        '''
        self.appendRow(ProjectItem(project))
        self.sort(0)
        if self.rowCount() == 1:
            qmindex = self.index(0, 0)
            
        # These actions should be governed by state change macro FIXME
        view.actions.project.close.CloseProjectAction().qaction.setEnabled(self.projects.rowCount() > 0)
        view.actions.project.save.SaveProjectAction().qaction.setEnabled(self.projectcache[self._get_name()].save)
        return project
        
        
    def closeProject(self, project):
        pass
        #FIXME: Search through qstandarditem names and remove match
        
    def saveProject(self, project):
        pass
        #FIXME: Search through qstandarditem names and saveProject
        
    #FIXME: the selected or active project should be held in a cache
    #       so any toolbar / actions will be applied to THAT project
        
    class ProjectItem(QtGui.QStandardItem):
        
        def __init__(self, project):
            super(ProjectItem, self).__init__(
                project.name, project.icon)
            self.project = project
            
        
        
        