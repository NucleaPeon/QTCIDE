from PyQt4 import QtGui, QtCore

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
            test = QtGui.QStandardItem(1, 2)
            test.setEditable(False)
            test.setText("gcc")
            self.rootNode.appendRow(test)
            self.compilertree = QtGui.QTreeView()
            self.compilertree.setModel(self.compilers)
            
            
        return self._instance