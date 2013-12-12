from PyQt4 import QtGui, QtCore

class Testing(QtGui.QDockWidget):
    
    def __init__(self):
        super(Testing, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Testing Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)