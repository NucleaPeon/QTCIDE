from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class ConfigureCompilerAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ConfigureCompilerAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-configure.png'))
            cls.qaction = QtGui.QAction(cls.qicon, 'Compiler &Configuration', None)
            cls.qaction.setStatusTip('Compiler Configuration')
            cls.qaction.triggered.connect(cls.compiler_config)
        return cls._instance

    @QtCore.pyqtSlot()
    def compiler_config():
        print("TODO popup window to configure a compiler")