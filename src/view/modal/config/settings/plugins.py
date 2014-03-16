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
        # Set up custom UI
        # Language Modules
        self.langmodules = QtGui.QGroupBox("Language Plugins")
        self.langlayout = QtGui.QVBoxLayout()
        self.langmodules.setLayout(self.langlayout)
        self.widgetlayout.addWidget(self.langmodules)
        
        self.langmodlist = QtGui.QListView()
        self.languages = QtGui.QStandardItemModel(0, 2)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        
        addbutton = QtGui.QPushButton(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'list-add.png')), '&Add Language')
        self.buttonBox.accepted.connect(self.accept)
        rembutton = QtGui.QPushButton(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'list-remove.png')), '&Remove Language')
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.addButton(addbutton, QtGui.QDialogButtonBox.YesRole)
        self.buttonBox.addButton(rembutton, QtGui.QDialogButtonBox.NoRole)
        
        self.langlayout.addWidget(self.langmodlist)
        self.langlayout.addWidget(self.buttonBox)
        self.widgetlayout.insertStretch(-1)
        
    def accept(self):
        print("Accept")
        #FIXME: add searching through folders recursively for languages
    
    def reject(self):
        print("Reject")
    
    def settings(self):
        return self.widget