from PyQt4 import QtGui, QtCore
import view.modal.config.ProjectSettingsPane
import conf.view.modal.config.settings
import os
from view.img import SYS_IMG_FOLDER

'''
Basic project settings

:Description:
    Settings module includes two views that depict what setting modules
    are being loaded, both custom and project default ones.
    
    
'''
class Project(view.modal.config.ProjectSettingsPane.ProjectSettingsPane):
    
    def __init__(self):
        super(view.modal.config.ProjectSettingsPane.ProjectSettingsPane, self).__init__("Project")
        self.widget = QtGui.QGroupBox("Project Settings")
        self.widgetlayout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.widgetlayout)
        # Project Loaded Setting Modules
        self.qidemodules = QtGui.QGroupBox("Default Setting Modules")
        self.custommodules = QtGui.QGroupBox("Custom Setting Modules")
        self.qidelayout = QtGui.QVBoxLayout()
        self.qidemodules.setLayout(self.qidelayout)
        self.customlayout = QtGui.QVBoxLayout()
        self.custommodules.setLayout(self.customlayout)
        self.widgetlayout.addWidget(self.qidemodules)
        self.widgetlayout.addWidget(self.custommodules)
        # Module Widgets
        self.qidesettingmodlist = QtGui.QListView()
        # Add model items to the view
        self.models = QtGui.QStandardItemModel(0, 1)
        for x in conf.view.modal.config.settings.qidesettings:
            self.models.appendRow(QtGui.QStandardItem(x))
        self.qidesettingmodlist.setModel(self.models)
        
        # Custom Module Widgets
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # Create buttons:
        addbutton = QtGui.QPushButton(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'list-add.png')), '&Add Module')
        self.buttonBox.accepted.connect(self.accept)
        rembutton = QtGui.QPushButton(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'list-remove.png')), '&Remove Module')
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.addButton(addbutton, QtGui.QDialogButtonBox.YesRole)
        self.buttonBox.addButton(rembutton, QtGui.QDialogButtonBox.NoRole)
        
        #self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)
        self.customsettingmodlist = QtGui.QListView()
        # Add model items to the view
        self.custommodels = QtGui.QStandardItemModel(0, 2)
        self.qidelayout.addWidget(self.qidesettingmodlist)
        self.customlayout.addWidget(self.customsettingmodlist)
        self.customlayout.addWidget(self.buttonBox)
        self.widgetlayout.insertStretch(-1)
        
    def accept(self):
        print("Accept")
    
    def reject(self):
        print("Reject")
        
    def settings(self):
        return self.widget
    