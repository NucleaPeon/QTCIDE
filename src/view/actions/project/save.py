from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import model.project
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class SaveProjectAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(SaveProjectAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'media-floppy.png'))
            cls.qaction = QtGui.QAction(cls.qicon,
                                        '&Save Project', None)
            cls.qaction.setShortcut('Ctrl-S')
            cls.qaction.setStatusTip('Save Project')
            cls.qaction.triggered.connect(cls.saveProject)
            cls.qaction.setEnabled(False)
        return cls._instance

    @QtCore.pyqtSlot(bool)
    def saveProject(triggered):
        model.project.Project().saveProject()
        
        