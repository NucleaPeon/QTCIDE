from PyQt4 import QtGui, QtCore
import model.compiler
import os

class Compiler(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Compiler, self).__new__(
                self, *args, **kwargs)
            self.widget = QtGui.QWidget()
            self.compilermodel = model.compiler.Compiler()
        return self._instance
    
    
    def __init__(self):
        super(Compiler, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.dockCompilerContents = QtGui.QWidget() #FIXME: This can go into its own module?
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join('res', 
                                             'system-run.png'))
        self.compilertree = model.compiler.Compiler().compilertree
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.compilertree)