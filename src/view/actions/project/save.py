from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import model.project
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class SaveProjectAction(QtGui.QAction):
    
    def __init__(self):
        super(SaveProjectAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'media-floppy.png')),
                                                                '&Save Project', None)
        self.setShortcut('Ctrl-S')
        self.setStatusTip('Save Project')
        self.triggered.connect(self.saveProject)

    @QtCore.pyqtSlot(bool)
    def saveProject(triggered):
        save = QtGui.QFileDialog.getSaveFileName(None, 'Save Project', os.environ.get("HOME"),
                                                 model.project.PROJECT_FILTER)
        model.project.Project().saveProject(name=save)
        
        