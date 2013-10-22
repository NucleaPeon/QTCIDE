from PyQt4 import QtGui, QtCore
import controller.settings as settings
import model.project

class ProjectDock(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        '''
        :Parameters:
            - args: list of model.project.Project() objects
        '''
        super().__init__()        
        self.projects = []
        self.projects.extend(args)
        # Initialize Graphical Components
        self.project_tree_widget = QtGui.QTreeView()
        # Initialize Model Components
        #     self.project_model contains a list of Project model's models
        self.project_model = QtGui.QStandardItemModel() 
        self.project_tree_widget.setModel(self.project_model)
        # TODO: Translation of Strings
        self.project_model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Project Name"))
        # Get all projects initialized in the Project Dock object
        for proj in self.projects:
            self.project_model.appendRow(QtGui.QStandardItem(proj.name))
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()
        # Initialize Project View (TreeView) and add it to this dock widget
        layout.addWidget(self.project_tree_widget)
        
    
    def createNewProject(self, name):
        '''
        :Description:
            Create a new project in the TreeModel
            
        :Parameters:
            - project_model; model.project.Project(): 
              
        '''
        # Add to stored array of projects
        self.projects.append(model.project.Project(name))
        # Now add to project tree widget
        self.project_model.appendRow(QtGui.QStandardItem(name))
        
    def closeSelectedProjects(self):
        '''
        :Description:
            Removes a project from the TreeModel, does not delete
            
        :Parameters:
            - project_model; string: name of Project
        '''
        itemsToRemove = self.project_tree_widget.selectedIndexes()
        for item in itemsToRemove:
            self.project_model.removeRow(item.row(), item.parent())
        
    def listAllProjects(self):
        return ', '.join(str(x) for x in self.projects)