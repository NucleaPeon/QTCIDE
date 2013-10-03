from PyQt4 import QtGui, QtCore
import src.base.settings as settings

class ProjectDock(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()