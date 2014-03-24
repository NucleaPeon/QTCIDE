from PyQt4 import QtGui, QtCore
import view.modal.config.window

class Project(QtGui.QStandardItemModel):

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args)
        self.projecttree = QtGui.QTreeView()
        self.projecttree.setModel(self)
        self.menu = view.menu.context.project.ProjectContextMenu(
            [])
        self.projecttree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setHorizontalHeaderItem(0, 
                QtGui.QStandardItem("Project Name"))
        self.connect(self.projecttree,
                QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
                self.menu.displayProjectMenu) 
        self.projecttree.connect(self.projecttree.selectionModel(),
                QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                self.__project_context)
        
        
    def __project_context(self):
        print("__project_context TODO")
        # FIXME: Create macros for context
        
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
        print(project)
        if project.icon is None:
            self.appendRow(QtGui.QStandardItem(project.name))
        else:
            self.appendRow(QtGui.QStandardItem(project.icon, project.name))
        
        # These actions should be governed by state change macro FIXME
        #view.actions.project.close.CloseProjectAction().setEnabled(self.projects.rowCount() > 0)
        #view.actions.project.save.SaveProjectAction().setEnabled(self.projectcache[self._get_name()].save)
        return project
        
        
    def closeProject(self, project):
        print("closeProject TODO")
        #FIXME: Search through qstandarditem names and remove match
        
    def saveProject(self, project):
        print("saveProject TODO")
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

    def configuration(self):
        view.modal.config.window.ProjectConfiguration().exec_()
        
    class ProjectItem(QtGui.QStandardItem):
        
        def __init__(self, project):
            super(ProjectItem, self).__init__(
                project.name, project.icon)
            self.project = project
            
        
        
        