from PyQt4 import QtGui, QtCore

class Terminal(QtGui.QDockWidget):
    
    def __init__(self):
        super(Terminal, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)