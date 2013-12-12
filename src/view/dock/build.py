from PyQt4 import QtGui, QtCore

class Build(QtGui.QDockWidget):
    
    def __init__(self):
        super(Build, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Build Options", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)