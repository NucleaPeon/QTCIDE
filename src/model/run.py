from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.actions.project.build.build as build
import view.menu.runcontext
import os

class Run:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Run, self).__new__(
                self, *args, **kwargs)
            self.runs = QtGui.QStandardItemModel() # Project data
            self.runs.setHorizontalHeaderItem(0, 
                                                  QtGui.QStandardItem("Run"))
            self.rootNode = self.runs.invisibleRootItem()
            self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'configure.png'))
            test = QtGui.QStandardItem(build.BuildSystemBuildAction().qicon, "gcc")
            test.setEditable(False)
            test.appendRow(QtGui.QStandardItem(self.qicon, "Test Build Configuration"))
            self.rootNode.appendRow(test)
            self.runtree = QtGui.QTreeView()
            self.runcontextmenu = view.menu.runcontext.RunContextMenu()
            self.runtree.setModel(self.runs)
        return self._instance