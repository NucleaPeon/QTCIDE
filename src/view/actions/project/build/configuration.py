from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class BuildSystemConfigurationAction(QtGui.QAction):
    
    
    def __init__(self):
        super(BuildSystemConfigurationAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build.png')),
                                                             '&Configuration', None)
        self.setStatusTip('Build Configuration')
        self.triggered.connect(self.configure)

    @QtCore.pyqtSlot(bool)
    def configure(triggered):
        print("TODO call model build module which can then call controller")