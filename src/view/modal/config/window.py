'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore
import view.modal.config.settings.project
import view.modal.config.settings.build
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
            cls.qidesettings = {'Project': view.modal.config.settings.project.Project(),
                                'Build': view.modal.config.settings.build.Build()}
            
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
        # --> Displays Setting panels
        self.innerwidget = QtGui.QWidget()
        self.settingspane = QtGui.QVBoxLayout()
        self.innerwidget.setLayout(self.settingspane)
        self.innerlayout.addWidget(self.innerwidget, 1, 2)
        self.innerwidget.setMinimumSize(400, 450)
        # <-- 
        
        
        self.layout.addWidget(self.objects)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)
        self.listview.connect(self.listview.selectionModel(),
                              QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                              self.selectionChanged)
        # Add the left-hand side bits: string and possibly icon for settings panel
        for x in self.qidesettings: # Dictionary keys
            # Adds all built in settings into model
            projsettingpane = self.qidesettings.get(x)
            projsettingpane.setEditable(False)
            self.model.appendRow(projsettingpane)
            widget = projsettingpane.settings()
            self.settingspane.addWidget(widget)
            widget.hide()
            

        # Select the first settings model
        mindex = self.model.index(0, 0)
        self.listview.setCurrentIndex(mindex) # selects first model
        
        
        # TODO: Select first item, display on 2nd pane, use selected
        # widget from selectionChanged method to display new item
        
    def selectionChanged(self, selected, deselected):
        '''
        Hide the widget that gets deselected and show widget that is selected
        '''
        if len(deselected.indexes()) > 0:
            self.qidesettings.get(deselected.indexes()[0].data()).settings().hide()
            
        widget = self.qidesettings.get(selected.indexes()[0].data()).settings()
        widget.show()
        