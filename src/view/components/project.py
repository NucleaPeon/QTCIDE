from PyQt4 import QtGui, QtCore

CACHE = ['Project']

class Project(QtGui.QStandardItemModel):

    
    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self.projecttree = QtGui.QTreeView()
        self.projecttree.setModel(self)
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
    
    def _get_name(self):
        '''
        :Description:
            Returns the text of the selected project from the model
            
        :Returns:
            String of the selected project name or None if no rows exist
        '''
        if self.projecttree.currentIndex().row() >= 0:
            return self.projects.item(self.projecttree.currentIndex().row()).text()

        
    class ProjectItem(QtGui.QStandardItem):
        
        def __init__(self, project):
            super(ProjectItem, self).__init__(
                project.name, project.icon)
            self.project = project
            
        
        
        