from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class RemoveTestSuiteAction(QtGui.QAction):
    
    def __init__(self):
        super(RemoveTestSuiteAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png')),
                                                    '&Remove Test Suite', None)
        self.setStatusTip('&Remove Test Suite')
        self.triggered.connect(self.rem_test_suite)

    @QtCore.pyqtSlot()
    def rem_test_suite(self):
        print('rem_test_suite')
        # TODO: Add action to menu and toolbar