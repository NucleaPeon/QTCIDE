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
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__()
        # Setup window content - layout
        ishell = view.main.widget.IntegratedShell()
        self.setCentralWidget(ishell)
        model = m.model(__name__)
        self.setWindowTitle(
            QtGui.QApplication.translate("QT-Based Drag and Drop IDE",
                "QT-Based Drag and Drop IDE", 
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.resize(model.width, model.height)
        self.setWindowIcon(QtGui.QIcon(SYS_APP_ICON))
        dock_project = view.dock.project.Project()
        dock_build = view.dock.build.Build()
        dock_terminal = view.dock.terminal.Terminal()
        dock_testing = view.dock.testing.Testing()
        dock_run = view.dock.run.Run()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), dock_project)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), dock_build)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), dock_terminal)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), dock_testing)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), dock_run)
        self.menubar = menu.MenuBar(self)
        
    def status(self, message):
        self.statusBar().showMessage(message)