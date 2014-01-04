from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class ConfigureTestSuiteAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ConfigureTestSuiteAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Configure Test Suite', None)
            cls.qaction.setStatusTip('&Configure Test Suite')
            cls.qaction.triggered.connect(cls.conf_test_suite)
        return cls._instance

    @QtCore.pyqtSlot()
    def conf_test_suite():
        #model.test.Test().add_test_suite()
        print('conf_test_suite')
        