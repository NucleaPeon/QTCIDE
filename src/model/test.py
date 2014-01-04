from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON

import os
class Test:
    
    _instance = None
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Test, self).__new__(
                self, *args, **kwargs)
            self.tests = QtGui.QStandardItemModel() # Project data
            self.tests.setHorizontalHeaderItem(0, QtGui.QStandardItem("Configurations"))
            self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'utilities-log-viewer.png'))
            self.testtree = QtGui.QTreeView()
            self.testtree.setModel(self.tests)
        return self._instance