from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class NewBuildSystemBuildAction(QtGui.QAction):
    
    
    def __init__(self):    
        super(NewBuildSystemBuildAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'system-run.png')),
                                                     '&Build', None)
        self.setStatusTip('Build Project')
        self.triggered.connect(self.build)
    

    @QtCore.pyqtSlot(bool)
    def build(triggered):
        print("TODO call model build module which can then call controller")