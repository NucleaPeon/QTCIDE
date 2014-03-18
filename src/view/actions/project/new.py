from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.modal.QtPopupTextInput
import view.window
import model.project
import os

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class NewProjectAction(QtGui.QAction):

    def __init__(self, *args, **kwargs):
        super(NewProjectAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'document-new.png')),
                                    '&New Project', None)
        self.setShortcut('Ctrl-N')
        self.setStatusTip('New Project')
        
        self.triggered.connect(self.promptNewProject)
            
    @QtCore.pyqtSlot(str)
    def promptNewProject(self):
        '''
        :Description:
            Create and run name prompt for new project
        '''
        modal = view.modal.QtPopupTextInput.QtPopupTextInput("QTCIDE", "Project Name:")
        modal.success(lambda: model.project.Project().addNewProject(modal.textline.text()))
        modal.exec_()