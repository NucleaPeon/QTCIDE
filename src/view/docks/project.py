from PyQt4 import QtGui, QtCore
import controller.settings as settings
import view.base.projectview as pview

class ProjectDock(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        '''
        :Parameters:
            - args: list of model.project.Project() objects
        '''
        super().__init__()
        self.projects = args
        # Initialize Graphical Components
        self.project_tree_widget = QtGui.QTreeView()
        # Initialize Model Components
        #     self.project_model contains a list of Project model's models
        self.project_model = QtGui.QStandardItemModel() 
        self.project_tree_widget.setModel(self.project_model)
        self.project_model.setHorizontalHeaderItem(0, QtGui.QStandardItem("Project Name"))
        # Get all projects initialized in the Project Dock object
        for proj in self.projects:
            self.project_tree_widget.appendRow(QtGui.QStandardItem(proj))
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()
        # Initialize Project View (TreeView) and add it to this dock widget
        layout.addWidget(self.project_tree_widget)
