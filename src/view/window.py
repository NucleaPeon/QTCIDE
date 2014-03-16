from PyQt4 import QtGui, QtCore
import model as m
import view.dock.project
import view.dock.build
import view.dock.run
import view.dock.testing
import view.dock.terminal
import view.menu.menu as menu
import view.main.widget
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON


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
        widget = view.main.widget.IntegratedShell()
        self.setCentralWidget(widget)
        
        model = m.model(__name__)
        self.setWindowTitle(
            QtGui.QApplication.translate("C and C++ Development Environment",
                "C and C++ Development Environment", 
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.resize(model.width, model.height)
        self.setWindowIcon(QtGui.QIcon(SYS_APP_ICON))
        self.project_dock = view.dock.project.Project()
        self.build_dock = view.dock.build.Build()
        self.terminal_dock = view.dock.terminal.Terminal()
        self.testing_dock = view.dock.testing.Testing()
        self.compiler_dock = view.dock.run.Run()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.project_dock)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.build_dock)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.compiler_dock)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.testing_dock)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.terminal_dock)
        self.menubar = menu.MenuBar(self)
        
    def status(self, message):
        self.statusBar().showMessage(message)