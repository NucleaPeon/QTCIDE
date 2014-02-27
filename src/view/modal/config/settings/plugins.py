'''
Plugin installation and linkage component
'''

from PyQt4 import QtGui, QtCore
import view.modal.config.ProjectSettingsPane
import os
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON

class Plugins(view.modal.config.ProjectSettingsPane.ProjectSettingsPane):
    
    def __init__(self):
        super(view.modal.config.ProjectSettingsPane.ProjectSettingsPane, self).__init__("Plugins")
        self.widget = QtGui.QWidget()
        self.widgetlayout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.widgetlayout)
        self.widgetlayout.addWidget(QtGui.QLabel("Plugin Information:"))
    
    def settings(self):
        return self.widget