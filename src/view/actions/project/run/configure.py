from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os
import model.run

class ConfigureRunAction(QtGui.QAction):

    def __init__(self):
            super(ConfigureRunAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'run-build-configure.png')),
                                                     'Run &Configuration', None)
            self.setStatusTip('Run Configuration')
            self.triggered.connect(self.run_config)

    @QtCore.pyqtSlot()
    def run_config(self):
        model.run.Run().configure_run()