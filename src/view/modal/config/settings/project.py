from PyQt4 import QtGui, QtCore
import view.modal.config.ProjectSettingsPane

'''
Basic project settings
'''

class Project(view.modal.config.ProjectSettingsPane.ProjectSettingsPane):
    
    def __init__(self):
        super(view.modal.config.ProjectSettingsPane.ProjectSettingsPane, self).__init__("Project")
        self.widget = QtGui.QGroupBox("Project Settings")
        self.widgetlayout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.widgetlayout)
        # Project Loaded Setting Modules
        self.qidemodules = QtGui.QGroupBox("QIDE Setting Modules")
        self.qidelayout = QtGui.QVBoxLayout()
        self.qidemodules.setLayout(self.qidelayout)
        
        
    def settings(self):
        return self.widget
    