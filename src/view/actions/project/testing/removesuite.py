from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class RemoveTestSuiteAction():
    
    def __init__(self):
        super(RemoveTestSuiteAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Remove Test Suite', None)
        self.qaction.setStatusTip('&Remove Test Suite')
        self.qaction.triggered.connect(self.rem_test_suite)

    @QtCore.pyqtSlot()
    def rem_test_suite():
        print('rem_test_suite')
        # TODO: Add action to menu and toolbar