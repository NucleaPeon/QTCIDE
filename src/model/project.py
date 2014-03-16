'''
Project Model

:Description:
    This project model is not a barebones model. It contains all the
    functionality for handling projects and data is saved in the
    cache

TODO: 
    - Validate that name is unique upon 
        a) rename of project
        b) new project
        
'''
from PyQt4 import QtGui, QtCore
import view.menu.context.project
import view.modal.config.window
import view.window
import controller.project
import model.data.project as data

PROJECT_FILTER = 'QTIDE Project (*.qtp)'

class Project:
    
    name = None
    icon = None
    languages_used = []
    saved = False
    path = os.environ.get("HOME")
    
        
    def configuration(self):
        view.modal.config.window.ProjectConfiguration().exec_()
        
        
    def _get_name(self):
        '''
        :Description:
            Returns the text of the selected project from the model
            
        :Returns:
            String of the selected project name or None if no rows exist
        '''
        if self.projecttree.currentIndex().row() >= 0:
            return self.projects.item(self.projecttree.currentIndex().row()).text()
