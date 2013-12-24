from PyQt4 import QtGui, QtCore
import model.compiler

'''
Compiler Contextual Menu, Right-Click on Compiler TreeView

When instantiated it will connect with the model.compiler
treeview component
'''
class CompilerContextMenu(QtGui.QMenu):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(CompilerContextMenu, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(CompilerContextMenu, self).__init__()
        #self.addAction(view.actions.project.new.NewProjectAction().qaction)
        #self.addAction(view.actions.project.close.CloseProjectAction().qaction)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayCompilertMenu(self, point):
        pass