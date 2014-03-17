from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class RemoveRunAction():
    
    def __init__(self):
        super(RemoveRunAction, self).__init__()
        self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'dialog-close.png'))
        self.qaction = QtGui.QAction(self.qicon, '&Remove Run', None)
        self.qaction.setStatusTip('&Remove Run')
        self.qaction.triggered.connect(self.rem_run_config)

    @QtCore.pyqtSlot()
    def rem_run_config():
        model.run.Run().remove_run_config()