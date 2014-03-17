from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.components.project
import importlib
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class ProjectSettingsAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ProjectSettingsAction, cls).__new__(cls)
            cls.qaction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'preferences-system-windows-actions.png')),
                                        'Project S&ettings', None)
            cls.qaction.setShortcut('Ctrl-E')
            cls.qaction.setStatusTip('Configure Project Settings')
            cls.qaction.triggered.connect(cls.projectSettings)
        return cls._instance

    @QtCore.pyqtSlot(bool)
    def projectSettings(triggered):
        project = importlib.import_module('cache').load('view.components.project.Project')
        project.configuration()