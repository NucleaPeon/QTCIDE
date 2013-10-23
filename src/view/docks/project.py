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
        self.projects = []
        self.projects.extend(args)
        # Initialize Graphical Components
        self.project_tree_widget = QtGui.QTreeView()
        self.project_tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.project_tree_widget, 
            QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), print) # self.displayProjectMenu)
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
        
    #@QtCore.pyqtSlot(QtCore.QPoint)
    #def displayProjectMenu(self, point):
        ## Get element under point
        #index = self.project_tree_widget.indexAt(point)
        #if not index.isValid():
            #return 
        
        #menu = QtGui.QMenu(self)
        #closeProject = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                              #'document-close.png')), 
                                                 #'&Close Project', self)
        
