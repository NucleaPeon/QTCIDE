from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class AddTestSuiteAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(AddTestSuiteAction, cls).__new__(cls)
            cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
            cls.qaction = QtGui.QAction(cls.qicon, '&Add Test Suite', None)
            cls.qaction.setStatusTip('&Add Test Suite')
            cls.qaction.triggered.connect(cls.add_test_suite)
        return cls._instance

    @QtCore.pyqtSlot()
    def add_test_suite():
        #model.test.Test().add_test_suite()
        print('add_test_suite')
        