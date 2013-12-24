from PyQt4 import QtGui, QtCore
import model.compiler
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.compilercontext
import controller.compiler
import os

class Compiler(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Compiler, self).__new__(
                self, *args, **kwargs)
            self.widget = QtGui.QWidget()
        return self._instance
    
    
    def __init__(self):
        super(Compiler, self).__init__()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.dockCompilerContents = QtGui.QWidget()
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'system-run.png'))
        self.compilertree = model.compiler.Compiler().compilertree
        self.compilertree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.compilertree)
        self.connect(self.compilertree,
                     QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"),
                     view.menu.compilercontext.CompilerContextMenu().displayCompilerMenu)
        
        print(self.compilertree)