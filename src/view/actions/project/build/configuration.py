from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class BuildSystemConfigurationAction():
    
    
    def __init__(self):
        self._instance = super(BuildSystemConfigurationAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Configuration', None)
        self.qaction.setStatusTip('Build Configuration')
        self.qaction.triggered.connect(self.configure)

    @QtCore.pyqtSlot(bool)
    def configure(triggered):
        print("TODO call model build module which can then call controller")