from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.actions.project.build.build as build
import view.menu.compilercontext
import os

class Compiler:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Compiler, self).__new__(
                self, *args, **kwargs)
            self.compilers = QtGui.QStandardItemModel() # Project data
            self.compilers.setHorizontalHeaderItem(0, 
                                                  QtGui.QStandardItem("Compiler"))
            self.rootNode = self.compilers.invisibleRootItem()
            self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'configure.png'))
            test = QtGui.QStandardItem(build.BuildSystemBuildAction().qicon, "gcc")
            test.setEditable(False)
            test.appendRow(QtGui.QStandardItem(self.qicon, "Test Build Configuration"))
            self.rootNode.appendRow(test)
            self.compilertree = QtGui.QTreeView()
            self.compilercontextmenu = view.menu.compilercontext.CompilerContextMenu()
            self.compilertree.setModel(self.compilers)
        return self._instance