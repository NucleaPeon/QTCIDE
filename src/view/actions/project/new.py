from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.modal.QtPopupTextInput as qtinput
import view.window
import model.project
import os        

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class NewProjectAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(NewProjectAction, cls).__new__(cls)
            cls.qaction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'document-new.png')),
                                        '&New Project', None)
            cls.qaction.setShortcut('Ctrl-N')
            cls.qaction.setStatusTip('New Project')
            cls.qaction.triggered.connect(cls.promptNewProject)
        return cls._instance

    def __init__(self):
        super(NewProjectAction, self).__init__()
        
    @QtCore.pyqtSlot(str)
    def promptNewProject(self):
        qtinput.getTextPopup(None, "QTCIDE", "Project Name:",
                             callback=model.project.Project().addNewProject)
        model.project.Project().projects.sort(0)
        