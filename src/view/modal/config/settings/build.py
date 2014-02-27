from PyQt4 import QtGui, QtCore
import view.modal.config.ProjectSettingsPane

class Build(view.modal.config.ProjectSettingsPane.ProjectSettingsPane):
    
    def __init__(self):
        super(view.modal.config.ProjectSettingsPane.ProjectSettingsPane, self).__init__("Build")
        self.widget = QtGui.QGroupBox("Build Settings")
        self.widgetlayout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.widgetlayout)
    
    def settings(self):
        return self.widget