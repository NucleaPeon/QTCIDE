from PyQt4 import QtGui, QtCore
import model.test
import view.menu.context.test

class Testing(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(cls,  *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Testing, cls).__new__(
                cls, *args, **kwargs)
            cls.widget = QtGui.QWidget()
        return cls._instance
    
    def __init__(self):
        super(Testing, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Testing Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.testtree = model.test.Test().testtree
        self.testtree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.testtree)
        self.connect(self.testtree,
                     QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"),
                     view.menu.context.test.TestingContextMenu().displayTestMenu)
        
        self.testtree.connect(self.testtree.selectionModel(),
                QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"),
                self.__test_context)
        self.hide() # Hide by default
        
        
    def __test_context(self, selected, deselected):
        print("test context")