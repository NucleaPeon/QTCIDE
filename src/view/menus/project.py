'''
ProjectMenu

:Description:
    Singleton method that hides and shows different project-related
    menu items based on the menu_type parameter and MENU_TYPES dict
    for memory improvements, an always-cached menu, code reuse and
    organization
    
    Note:
        - This singleton class initializes graphical elements, so
          in order for callbacks to be properly set to the actions
          on these elements, they are assigned by receiving *args
          of objects that contain the callbacks and names.
          
    
    
'''
from PyQt4 import QtGui
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.docks.project as project
import os

ICONS = {}

class ProjectMenu():
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ProjectMenu, cls).__new__(*args, **kwargs)
            cls.menu = QtGui.QMenu()
        return cls._instance
       
    def __init__(self, *args, **kwargs):
        self.menu = 
        self.closeProject = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                             'document-close.png')), 
                                         '&Close Project', self)
        self.closeProject.triggered.connect(self.closeSelectedProjects)
        self.menu.addAction(self.closeProject)
        
        
    def menu(self):
        self.menu.popup(QtGui.QCursor.pos())
        
    def closeSelectedProjects(self):
        '''
        :Description:
            Removes a project from the TreeModel, does not delete
        '''
        itemsToRemove = self.project_tree_widget.selectedIndexes()
        for item in itemsToRemove:
            self.project_model.removeRow(item.row(), 
                                         self.project_tree_widget.rootIndex())
            
    def listAllProjects(self):
        return ', '.join(str(x) for x in self.projects)
    