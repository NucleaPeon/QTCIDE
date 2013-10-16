from PyQt4 import QtGui, QtCore, Qt
import os

class QtcideProjectView(QtGui.QTreeView):
    
    def __init__(self):
        super().__init__()
        self.model_projfiles = QtGui.QStandardItemModel()
        self.root_item = self.model_projfiles.invisibleRootItem()
        self.setModel(self.model_projfiles)
        self.model_projfiles.setHorizontalHeaderItem(0, QtGui.QStandardItem(""))
        self.model_projfiles.appendRow(QtGui.QStandardItem("name"))
        
    def newProject(self, name):
        self.model_projfiles.appendRow(QtGui.QStandardItem("name"))
        return str(repr(self.model_projfiles))