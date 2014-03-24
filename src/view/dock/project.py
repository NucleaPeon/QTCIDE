from PyQt4 import QtGui, QtCore
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.project
import controller.project
import os

class Project(QtGui.QDockWidget):

    SELECTED = None

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__()
        self.widget = QtGui.QWidget()
        # Set up dock
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'folder-development.png'))
        # Initialize TreeView for model to sit in
        
        self.project = self.ProjectModel()
        
        self.project.projecttree.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.project.projecttree)
        
    def add_project_to_view(self, model):
        '''
        Convenience method to add projects
        :Parameters:
            - model: model.project.Project

        :See:
            view.components.project.Project
        '''
        self.project.addProject(model)
        
    def select_project(self, index=0):
        '''
        Selects (by default) the first item in the view
        
        :Parameters:
            - index: row number starting at 0 (defaults to 0)
        '''
        qmindex = self.project.index(index, 0)
        self.project.projecttree.setCurrentIndex(qmindex)
        self.project.sort(0)
        
    def show_settings(self):
        '''
        Display Project Settings window
        '''
        view.modal.config.window.ProjectConfiguration().exec_()
        
        
    class ProjectModel(QtGui.QStandardItemModel):

        def __init__(self, *args, **kwargs):
            super(Project.ProjectModel, self).__init__(*args)
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

        class ProjectItem(QtGui.QStandardItem):
            
            def __init__(self, project):
                super(ProjectItem, self).__init__(
                    project.name, project.icon)
                self.project = project
                
            
            
            