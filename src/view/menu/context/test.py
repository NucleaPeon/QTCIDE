from PyQt4 import QtGui, QtCore
import model.test

class TestingContextMenu(QtGui.QMenu):
    
    _instance = None
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(TestingContextMenu, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(TestingContextMenu, self).__init__()
        #self.addAction(view.actions.project.testing.addsuite.AddTestSuiteAction())
        #self.addAction(view.actions.project.testing.configuresuite.ConfigureTestSuiteAction())
        #self.addAction(view.actions.project.testing.removesuite.RemoveTestSuiteAction())
        
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayTestMenu(self, point):
        index = model.test.Test().testtree.indexAt(point)
        self.popup(QtGui.QCursor.pos())