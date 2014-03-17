from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class ConfigureTestSuiteAction():
    
    def __init__(self):
        super(ConfigureTestSuiteAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Configure Test Suite', None)
        self.qaction.setStatusTip('&Configure Test Suite')
        self.qaction.triggered.connect(self.conf_test_suite)

    @QtCore.pyqtSlot()
    def conf_test_suite():
        #model.test.Test().add_test_suite()
        print('conf_test_suite')
        