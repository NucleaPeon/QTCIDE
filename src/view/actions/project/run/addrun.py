from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class AddRunAction(QtGui.QAction):
    
    
    def __init__(self):
        super(AddRunAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-file.png')),
                                           '&Add Run', None)
        self.setStatusTip('&Add Run')
        self.triggered.connect(self.add_run_config)

    @QtCore.pyqtSlot()
    def add_run_config(self):
        model.run.Run().add_run_config()
        