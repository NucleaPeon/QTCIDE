from PyQt4 import QtGui, QtCore
import view.actions.project.testing.addsuite
import model.test

class Testing(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Testing, self).__new__(
                self, *args, **kwargs)
            self.widget = QtGui.QWidget()
        return self._instance
    
    def __init__(self):
        super(Testing, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Testing Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.testtree = model.test.Test().testtree
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.testtree)
        
        