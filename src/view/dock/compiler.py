from PyQt4 import QtGui, QtCore

class Compiler(QtGui.QDockWidget):
    
    def __init__(self):
        super(Compiler, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.dockCompilerContents = QtGui.QWidget() #FIXME: This can go into its own module?
        self.setWidget(self.widget)