from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class BuildSystemBuildAction():
    
    
    def __init__(self, *args, **kwargs):    
        super(BuildSystemBuildAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'system-run.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Build', None)
        self.qaction.setStatusTip('Build Project')
        self.qaction.triggered.connect(self.build)
    

    @QtCore.pyqtSlot(bool)
    def build(triggered):
        print("TODO call model build module which can then call controller")