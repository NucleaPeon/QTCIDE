from PyQt4 import QtGui, QtCore
import controller.settings as settings
import controller.project as projcontrol
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import sys



class ProjectDock(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        '''
        :Parameters:
            - args: list of model.project.Project() objects
        '''
        super().__init__()
        # Cache the projecticon for fast generation of this icon
        self.ProjectIcon = QtGui.QIcon('res/folder-development.png')
        # Initialize Graphical Components
        self.project_tree_widget = QtGui.QTreeView()
        self.project_tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.project_tree_widget, 
            QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
            self.displayProjectMenu)
        # Initialize Model Components
        #     self.project_model contains a list of Project model's models
        self.project_model = QtGui.QStandardItemModel() 
        self.project_tree_widget.setModel(self.project_model)
        # TODO: Translation of Strings
        self.project_model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Project Name"))
        # Get all projects initialized in the Project Dock object
        for proj in projcontrol.PROJECTS.keys():
            self.project_model.appendRow(QtGui.QStandardItem(proj.name))
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()
        # Initialize Project View (TreeView) and add it to this dock widget
        layout.addWidget(self.project_tree_widget)
        
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        # Get element under point
        index = self.project_tree_widget.indexAt(point)
        if not index.isValid():
            return 
        
        menu = QtGui.QMenu(self)
        closeProject = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                              'document-close.png')), 
                                                 '&Close Project', self)
        menu.addAction(closeProject)
        closeProject.triggered.connect(self.closeSelectedProjects)
        menu.popup(QtGui.QCursor.pos())
        
    @QtCore.pyqtSlot(str)
    def createNewProject(self, name):
        '''
        :Description:
            Create a new project in the TreeModel
            
        :Parameters:
            - project_model; model.project.Project(): 
              
        '''
        # Add to stored array of projects
        if not name:
            return
        
        # Now add to project tree widget
        proj = projcontrol.initialize_project(name, 
                                              icon=QtGui.QIcon(self.ProjectIcon))
        self.project_model.appendRow(QtGui.QStandardItem(proj.icon, 
                                                         proj.name))
        
    @QtCore.pyqtSlot()
    def closeSelectedProjects(self):
        '''
        :Description:
            Removes a project from the TreeModel, does not delete
        '''
        itemsToRemove = self.project_tree_widget.selectedIndexes()
        for item in itemsToRemove:
            self.project_model.removeRow(item.row(), 
                                         self.project_tree_widget.rootIndex())