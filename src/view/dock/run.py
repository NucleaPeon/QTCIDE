from PyQt4 import QtGui, QtCore
import model.run
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.menu.context.run
import controller.run
import os

class Run(QtGui.QDockWidget):
    
    
    def __init__(self, *args, **kwargs):
        super(Run, self).__init__()
        self.widget = QtGui.QWidget()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.setWidget(self.widget)
        self.icon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 
                                             'system-run.png'))
        self.runtree = model.run.Run().runtree
        self.runtree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.runtree)
        self.connect(self.runtree,
                     QtCore.SIGNAL("customContextMenuRequested(const QPoint &)"),
                     view.menu.context.run.RunContextMenu().displayRunMenu)
        self.hide() # Hide by default