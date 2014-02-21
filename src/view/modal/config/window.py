'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore
import view.modal.config.settings.project
import importlib
import os

class ProjectConfiguration(QtGui.QDialog):
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ProjectConfiguration, cls).__new__(cls)
            cls.buttonBox = QtGui.QDialogButtonBox()
            cls.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            cls.buttonBox.setStandardButtons(
                QtGui.QDialogButtonBox.Cancel |
                QtGui.QDialogButtonBox.Apply | 
                QtGui.QDialogButtonBox.Ok)
            cls.buttonBox.accepted.connect(cls.accept)
            cls.buttonBox.rejected.connect(cls.reject)
            
        return cls._instance
    
    def __init__(self, title="Project Settings"):
        super(ProjectConfiguration, self).__init__()
        self.model = QtGui.QStandardItemModel()
        self.layout = QtGui.QVBoxLayout()
        self.innerlayout = QtGui.QGridLayout()
        self.objects = QtGui.QWidget()
        self.objects.setMinimumSize(200, 400)
        self.objects.setLayout(self.innerlayout)
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.listview = QtGui.QListView()
        self.listview.setModel(self.model)
        self.innerlayout.addWidget(self.listview, 1, 1)
        self.view = QtGui.QWidget()
        self.view.setMinimumSize(450, 400)
        self.innerlayout.addWidget(self.view, 1, 2)
        self.layout.addWidget(self.objects)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)
        
        #FIXME: Dynamic importlib module generation
        # Put in for loop
        self.listview.connect(self.listview.selectionModel(),
                              QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                              self.selectionChanged)
        settingspane = view.modal.config.settings.project.Project()
        settingspane.setEditable(False)
        self.model.appendRow(settingspane)
        # Set Selection to the first model if found
        if self.model.rowCount() >= 1:
            qmindex = self.model.index(0, 0)
            self.listview.setCurrentIndex(qmindex)
            # FIXME: Hardcoding what gets displayed, remove and go based on selected component
            self.display_widget(settingspane)
      
    def display_widget(self, widget):
        '''
        :Description:
            Display Widget on right-hand side of pane, 
            clears and re-adds widget so panel is refreshed.
            
            TODO: Use show() and hide() to save memory in all
            loaded module settings
        '''
        # FIXME FIXME FIXME
        self.innerlayout.removeWidget(self.view)
        self.view = widget.settings()
        self.view.setMinimumSize(450, 400)
        self.innerlayout.addWidget(self.view, 1, 2)
        # USE GRID LAYOUT AND REFRESH GRID ITEMS
        #TODO: Can this be more efficient? Different layout use?
        
        
        
    def selectionChanged(self, selected, deselected):
        pass
        # FIXME: May be required to cast before attempting to display gui
    
