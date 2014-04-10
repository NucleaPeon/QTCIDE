from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class NewTestSuiteAction(QtGui.QAction):
    
    def __init__(self):
        super(NewTestSuiteAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png')),
                                                 '&Add Test Suite', None)
        self.setStatusTip('&Add Test Suite')
        self.triggered.connect(self.add_test_suite)

    @QtCore.pyqtSlot()
    def add_test_suite(self):
        #model.test.Test().add_test_suite()
        print('add_test_suite')
        