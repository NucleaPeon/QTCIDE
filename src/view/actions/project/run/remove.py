from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class RemoveRunAction(QtGui.QAction):
    
    def __init__(self):
        super(RemoveRunAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'dialog-close.png')),
                                              '&Remove Run', None)
        self.setStatusTip('&Remove Run')
        self.triggered.connect(self.rem_run_config)

    @QtCore.pyqtSlot()
    def rem_run_config(self):
        model.run.Run().remove_run_config()