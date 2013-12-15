from PyQt4 import QtGui, QtCore
import model.project

'''
Project Contextual Menu, Right-Click on Project TreeView

When instantiated it will connect with the model.project
treeview component
'''
class ProjectContextMenu:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(ProjectContextMenu, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        print(index)