from PyQt4 import QtGui, QtCore
import src.base.settings as settings
import src.base.projectview as pview

class ProjectDock(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(layout)
        layout.addWidget(pview.QtcideProjectView())
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()
        
    @staticmethod
    def testProjectDbus():
        return "Test Complete"