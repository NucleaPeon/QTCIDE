from PyQt4 import QtGui, QtCore, Qt
import os

class QtcideProjectView(QtGui.QTreeView):
    
    def __init__(self):
        super().__init__()
        self.model_projfiles = QtGui.QStandardItemModel()
        self.root_item = self.model_projfiles.invisibleRootItem()
        self.setModel(self.model_projfiles)
        self.model_projfiles.setHorizontalHeaderItem(0, QtGui.QStandardItem("Projects"))
        
        self.model_projfiles.appendRow(QtGui.QStandardItem("Hello World"))
        