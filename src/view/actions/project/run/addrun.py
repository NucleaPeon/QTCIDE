from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class AddRunAction():
    
    
    _instance = None
    def __init__(self):
        super(AddRunAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-file.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Add Run', None)
        self.qaction.setStatusTip('&Add Run')
        self.qaction.triggered.connect(self.add_run_config)

    @QtCore.pyqtSlot()
    def add_run_config():
        model.run.Run().add_run_config()
        