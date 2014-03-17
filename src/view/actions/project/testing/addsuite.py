from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class AddTestSuiteAction():
    
    def __init__(self):
        super(AddTestSuiteAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Add Test Suite', None)
        self.qaction.setStatusTip('&Add Test Suite')
        self.qaction.triggered.connect(self.add_test_suite)

    @QtCore.pyqtSlot()
    def add_test_suite():
        #model.test.Test().add_test_suite()
        print('add_test_suite')
        