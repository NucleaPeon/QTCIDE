from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class ConfigureRunAction():

    def __init__(self):
            super(ConfigureRunAction, self).__init__()
            self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-configure.png'))
            self.qaction = QtGui.QAction(self.qicon, 'Run &Configuration', None)
            self.qaction.setStatusTip('Run Configuration')
            self.qaction.triggered.connect(self.run_config)

    @QtCore.pyqtSlot()
    def run_config():
        model.run.Run().configure_run()