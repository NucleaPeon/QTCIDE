from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import model.project
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class OpenProjectAction(QtGui.QAction):
    
    def __init__(self):
        super(OpenProjectAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'media-floppy.png')),
                                                                '&Open Project', None)
        self.setShortcut('Ctrl-O')
        self.setStatusTip('Open Project')
        self.triggered.connect(self.openProject)

    @QtCore.pyqtSlot(bool)
    def openProject(triggered):
        openfile = QtGui.QFileDialog.getOpenFileName(None, 'Open Project', os.environ.get("HOME"),
                                                 model.project.PROJECT_FILTER)
        if not openfile:
            print("Cancelled")
        print(openfile)
        
        