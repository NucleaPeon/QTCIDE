from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class BuildSystemConfigurationAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(BuildSystemConfigurationAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Configuration', None)
            cls.qaction.setStatusTip('Build Configuration')
            cls.qaction.triggered.connect(cls.build)
        return cls._instance

    @QtCore.pyqtSlot(bool)
    def build(triggered):
        print("TODO call model build module which can then call controller")