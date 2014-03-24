from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class ProjectSettingsAction(QtGui.QAction):
    
    
    def __init__(self):
        super(ProjectSettingsAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'preferences-system-windows-actions.png')),
                                    'Project S&ettings', None)
        self.setShortcut('Ctrl-E')
        self.setStatusTip('Configure Project Settings')
        self.triggered.connect(self.projectSettings)

    @QtCore.pyqtSlot(bool)
    def projectSettings(triggered):
        print("FIXME")