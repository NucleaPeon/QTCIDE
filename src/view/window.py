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
        kwargs['view.main.widget.IntegratedShell'] = view.main.widget.IntegratedShell()
        self.setCentralWidget(kwargs['view.main.widget.IntegratedShell'])
        kwargs['view.window.Window'] = self
        
        model = m.model(__name__)
        self.setWindowTitle(
            QtGui.QApplication.translate("QT-Based Drag and Drop IDE",
                "QT-Based Drag and Drop IDE", 
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.resize(model.width, model.height)
        self.setWindowIcon(QtGui.QIcon(SYS_APP_ICON))
        kwargs['view.dock.project.Project'] = view.dock.project.Project(**kwargs)
        kwargs['view.dock.build.Build'] = view.dock.build.Build()
        kwargs['view.dock.terminal.Terminal'] = view.dock.terminal.Terminal()
        kwargs['view.dock.testing.Testing'] = view.dock.testing.Testing()
        kwargs['view.dock.run.Run'] = view.dock.run.Run()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), kwargs['view.dock.project.Project'])
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), kwargs['view.dock.build.Build'])
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), kwargs['view.dock.terminal.Terminal'])
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), kwargs['view.dock.testing.Testing'])
        self.addDockWidget(QtCore.Qt.DockWidgetArea(8), kwargs['view.dock.run.Run'])
        self.menubar = menu.MenuBar(self)
        
    def status(self, message):
        self.statusBar().showMessage(message)