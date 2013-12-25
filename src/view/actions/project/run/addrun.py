from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class AddRunAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(AddRunAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-file.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Add Run', None)
            cls.qaction.setStatusTip('&Add Run')
            cls.qaction.triggered.connect(cls.add_run)
        return cls._instance

    @QtCore.pyqtSlot()
    def add_run():
        print("TODO popup window to add a run")