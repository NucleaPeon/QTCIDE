from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import model.project
import os


"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class CloseProjectAction(QtGui.QAction):
    
    def __init__(self):
        super(CloseProjectAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'document-close.png')),
                                    '&Close Project', None)
        self.setShortcut('Ctrl-C')
        self.setStatusTip('Close Project')
        self.triggered.connect(self.closeProject)
        self.setEnabled(False)
        

    @QtCore.pyqtSlot(bool)
    def closeProject(triggered):
        model.project.Project().closeProject()