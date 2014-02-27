'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore
import conf.view.modal.config.settings
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
            '''
            cls.qidesettings contains the instantiated copies of the references
            defined in the configuration file; conf files cannot hold instantiated
            references with PyQt4 because they are created outside the scope of
            the application.
            
            Therefore we are basically caching the entire thing twice:
                - configuration module determines what settings get loaded through references
                - this module determines and caches the gui portions that are displayed 
            '''
            cls.qidesettings = conf.view.modal.config.settings.qidesettings
            for x in conf.view.modal.config.settings.qidesettings:
                # Set all keys with instantiated items of class references
                cls.qidesettings[x] = conf.view.modal.config.settings.qidesettings.get(x)()
            # Add models, components, and connections
            cls.model = QtGui.QStandardItemModel()
            cls.layout = QtGui.QVBoxLayout()
            cls.innerlayout = QtGui.QGridLayout()
            cls.objects = QtGui.QWidget()
            cls.objects.setMinimumSize(200, 400)
            cls.objects.setLayout(cls.innerlayout)
            cls.listview = QtGui.QListView()
            cls.listview.setModel(cls.model)
            cls.innerlayout.addWidget(cls.listview, 1, 1)
            # --> Displays Setting panels
            cls.innerwidget = QtGui.QWidget()
            cls.settingspane = QtGui.QVBoxLayout()
            cls.innerwidget.setLayout(cls.settingspane)
            cls.innerlayout.addWidget(cls.innerwidget, 1, 2)
            cls.innerwidget.setMinimumSize(400, 450)
            # <-- 
            cls.layout.addWidget(cls.objects)
            cls.layout.addWidget(cls.buttonBox)
            
            # Add the left-hand side bits: string and possibly icon for settings panel
            for x in cls.qidesettings: # Dictionary keys
                # Adds all built in settings into model
                projsettingpane = cls.qidesettings.get(x)
                projsettingpane.setEditable(False)
                cls.model.appendRow(projsettingpane)
                widget = projsettingpane.settings()
                cls.settingspane.addWidget(widget)
                widget.hide()
                mindex = cls.model.index(0, 0)
                cls.listview.setCurrentIndex(mindex) # selects first model
            
        return cls._instance
    
    def __init__(self, title="Project Settings"):
        super(ProjectConfiguration, self).__init__()
        # Must disconnect and reconnect so only one invocation is
        # ever made.
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setLayout(self.layout)
        
        self.setWindowTitle(title)
        self.listview.connect(self.listview.selectionModel(),
                    QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                    self.selectionChanged)
        
        '''
        This code is required to fix bug where dialog box was empty when requested
        a second time.
        (By selecting another item in the list, then back to the first item,
         it would display. However, that will not work in a production env.)
        Problem involved moving a lot of initialization code to __new__, except
        connections between objects and parent object handling, which is
        done in __init__.
        
        By creating and selecting the first index, then forcefully showing
        the widget (as selectionChanged() when dialog opens fails to display it),
        the dialog box retains its integrity throughout multiple openings.
        '''
        mindex = self.model.index(0, 0)
        self.listview.setCurrentIndex(mindex) # selects first model
        widget = self.qidesettings.get(self.listview.selectedIndexes()[0].data()).settings()
        widget.show()
        ''' End of selection code to show Project widget '''
        
    def selectionChanged(self, selected, deselected):
        '''
        Hide the widget that gets deselected and show widget that is selected
        '''
        if len(deselected.indexes()) > 0:
            self.qidesettings.get(deselected.indexes()[0].data()).settings().hide()
        widget = self.qidesettings.get(selected.indexes()[0].data()).settings()
        widget.show()
        