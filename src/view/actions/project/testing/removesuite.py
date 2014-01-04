from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class RemoveTestSuiteAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(RemoveTestSuiteAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Remove Test Suite', None)
            cls.qaction.setStatusTip('&Remove Test Suite')
            cls.qaction.triggered.connect(cls.rem_test_suite)
        return cls._instance

    @QtCore.pyqtSlot()
    def rem_test_suite():
        #model.test.Test().add_test_suite()
        print('rem_test_suite')
        # TODO: Add action to menu and toolbar