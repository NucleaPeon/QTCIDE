from PyQt4 import QtGui, QtCore
import model.project
import view.actions.project.new
import view.actions.project.close

'''
Project Contextual Menu, Right-Click on Project TreeView

When instantiated it will connect with the model.project
treeview component
'''
class ProjectContextMenu(QtGui.QMenu):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(ProjectContextMenu, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(ProjectContextMenu, self).__init__()
        self.addAction(view.actions.project.new.NewProjectAction().qaction)
        self.addAction(view.actions.project.close.CloseProjectAction().qaction)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        self.clear()
        index = model.project.Project().projecttree.indexAt(point)
        self.addAction(view.actions.project.new.NewProjectAction().qaction)
        if index.isValid():
            self.addAction(view.actions.project.close.CloseProjectAction().qaction)
        self.popup(QtGui.QCursor.pos())
        