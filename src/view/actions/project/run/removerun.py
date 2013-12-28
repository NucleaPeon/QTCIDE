from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class RemoveRunAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(RemoveRunAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'dialog-close.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Remove Run', None)
            cls.qaction.setStatusTip('&Remove Run')
            cls.qaction.triggered.connect(cls.rem_run_config)
        return cls._instance

    @QtCore.pyqtSlot()
    def rem_run_config():
        model.run.Run().remove_run_config()