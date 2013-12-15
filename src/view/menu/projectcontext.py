from PyQt4 import QtGui, QtCore
import view.dock.project

'''
Project Contextual Menu, Right-Click on Project TreeView
'''
class ProjectContextMenu:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(ProjectContextMenu, self).__new__(
                self, *args, **kwargs)
            self.connect(self.project_tree_widget, #FIXME
                QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"), 
                self.displayProjectMenu)
        return self._instance
    
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        index = view.dock.project.Project().projecttree.indexAt(point)
        print(index)