from PyQt4 import QtGui, QtCore
import model.run

'''
Compiler Contextual Menu, Right-Click on Compiler TreeView

When instantiated it will connect with the model.compiler
treeview component
'''
class RunContextMenu(QtGui.QMenu):
    
    
    def __init__(self):
        super(RunContextMenu, self).__init__()
        #self.addAction(view.actions.project.run.addrun.AddRunAction())
        #self.addAction(view.actions.project.run.configurerun.ConfigureRunAction())
        #self.addAction(view.actions.project.run.removerun.RemoveRunAction())
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayRunMenu(self, point):
        index = model.run.Run().runtree.indexAt(point)
        self.popup(QtGui.QCursor.pos())