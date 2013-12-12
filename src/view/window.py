from PyQt4 import QtGui, QtCore
import model as m

'''
Window View

Contains the visual content of the main window.

Only one window should exist at one time per instance. Other modal windows 
should use QDialogs. 
'''
class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        # Setup window content - layout
        widget = QtGui.QWidget()
        layout = QtGui.QGridLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        model = m.model(__name__)
        self.setWindowTitle(
            QtGui.QApplication.translate("C and C++ Development Environment",
                "C and C++ Development Environment", 
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.resize(model.width, model.height)