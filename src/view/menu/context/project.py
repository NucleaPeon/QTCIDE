from PyQt4 import QtGui, QtCore
import view.components.project
import view.actions.project.new
import view.actions.project.close
import cache

CACHE = ['ProjectContextMenu']

'''
Project Contextual Menu, Right-Click on Project TreeView

When instantiated it will connect with the model.project
treeview component
'''
class ProjectContextMenu(QtGui.QMenu):
    
    def __init__(self):
        super(ProjectContextMenu, self).__init__()
        self.addAction(view.actions.project.new.NewProjectAction().qaction)
        self.addAction(view.actions.project.close.CloseProjectAction().qaction)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        project = cache.load('view.components.project.Project')
        index = project.projecttree.indexAt(point)
        self.popup(QtGui.QCursor.pos())
        