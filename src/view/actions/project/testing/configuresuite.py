from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class ConfigureTestSuiteAction(QtGui.QAction):
    
    def __init__(self):
        super(ConfigureTestSuiteAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png')),
                                                       '&Configure Test Suite', None)
        self.setStatusTip('&Configure Test Suite')
        self.triggered.connect(self.conf_test_suite)

    @QtCore.pyqtSlot()
    def conf_test_suite(self):
        #model.test.Test().add_test_suite()
        print('conf_test_suite')
        