from PyQt4 import QtGui, QtCore
import model as m
import view.main.dock_manager
import view.menu.menu as menu
import view.main.widget
import view.main.action_manager
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
        self.action_mgr = view.main.action_manager.ActionManager()
        model = m.model(__name__)
        self.setWindowTitle(
            QtGui.QApplication.translate("QT-Based Drag and Drop IDE",
                "QT-Based Drag and Drop IDE", 
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.resize(model.width, model.height)
        self.setWindowIcon(QtGui.QIcon(SYS_APP_ICON))
        self.menubar = menu.MenuBar(self)
        self.docks = view.main.dock_manager.DockManager()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.docks.PROJECT_DOCK)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.docks.BUILD_DOCK)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.docks.TERMINAL_DOCK)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.docks.TESTING_DOCK)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.docks.RUN_DOCK)
        self.ishell = view.main.widget.IntegratedShell()
        self.setCentralWidget(self.ishell)
        
    def status(self, message):
        self.statusBar().showMessage(message)