from PyQt4 import QtGui, QtCore
import model.project
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.project
import controller.project
import os

class Project(QtGui.QDockWidget):

    '''
    :Description:
        - Contains an index of the view that holds the object
    '''
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
                    self.selectionChanged)
            
            
        def selectionChanged(self, selected, deselected):
            if selected.count() == 1:
                Project.SELECTED = selected.indexes()[0]
            print(self.itemFromIndex(Project.SELECTED).project)
            
            
        def addProject(self, project_name):
            '''
            Adds a project to the graphical view based on the model
            
            :Description:
                Checks project information, verifies, and adds project
                to the model/view ui representation.
                
                Verification includes:
                    - proper name format
                    - including icon in QStandardItem
            
            :Parameters:
                - project_name: string name of project to add
            '''
            stditem = Project.ProjectItem(project_name)
            self.appendRow(stditem)
            index = self.indexFromItem(stditem)
            self.projecttree.setCurrentIndex(index)
            
            
        def closeProject(self, project):
            print("closeProject TODO")
            #FIXME: Search through qstandarditem names and remove match
            
        def saveProject(self, project):
            print("saveProject TODO")
            #FIXME: Search through qstandarditem names and saveProject

    class ProjectItem(QtGui.QStandardItem):
        
        def __init__(self, project):
            super(Project.ProjectItem, self).__init__(
                QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'media-floppy.png')),
                                                                project)
            self.project = project
        
            
            
            