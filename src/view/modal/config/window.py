'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore
import importlib
import os

### Imports to Remove Later
import view.modal.config.settings.project as project

###

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
        self.innerlayout = QtGui.QHBoxLayout()
        self.objects = QtGui.QWidget()
        self.objects.setMinimumSize(200, 400)
        self.objects.setLayout(self.innerlayout)
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.listview = QtGui.QListView()
        self.listview.setModel(self.model)
        self.innerlayout.addWidget(self.listview)
        self.view = QtGui.QWidget()
        self.view.setMinimumSize(450, 400)
        self.innerlayout.addWidget(self.view)
        self.layout.addWidget(self.objects)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)
        
        #FIXME: Dynamic importlib module generation
        # Put in for loop
        self.listview.connect(self.listview.selectionModel(),
                              QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                              self.selectionChanged)
        settingspane = QtGui.QStandardItem(project.Project()._Name_)
        settingspane.setEditable(False)
        self.model.appendRow(settingspane)
        # Set Selection to the first model if found
        if self.model.rowCount() == 1:
            qmindex = self.model.index(0, 0)
            self.listview.setCurrentIndex(qmindex)
        
        
    def selectionChanged(self, selected, deselected):
        print(self)
    