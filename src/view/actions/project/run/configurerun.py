from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class ConfigureRunAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ConfigureRunAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-configure.png'))
            cls.qaction = QtGui.QAction(cls.qicon, 'Run &Configuration', None)
            cls.qaction.setStatusTip('Run Configuration')
            cls.qaction.triggered.connect(cls.run_config)
        return cls._instance

    @QtCore.pyqtSlot()
    def run_config():
        model.run.Run().configure_run()