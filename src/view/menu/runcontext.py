from PyQt4 import QtGui, QtCore
import view.actions.project.run.addrun
import view.actions.project.run.configurerun
import model.run

'''
Compiler Contextual Menu, Right-Click on Compiler TreeView

When instantiated it will connect with the model.compiler
treeview component
'''
class RunContextMenu(QtGui.QMenu):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(RunContextMenu, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(RunContextMenu, self).__init__()
        self.addAction(view.actions.project.run.addrun.AddRunAction().qaction)
        self.addAction(view.actions.project.run.configurerun.ConfigureRunAction().qaction)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayRunMenu(self, point):
        index = model.run.Run().runtree.indexAt(point)
        self.popup(QtGui.QCursor.pos())