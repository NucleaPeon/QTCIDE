from PyQt4 import QtGui, QtCore
import src.base.settings as settings
import src.base.projectview as pview

class ProjectDock(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.qtcproject = pview.QtcideProjectView()
        layout.addWidget(self.qtcproject)
        self.settings = settings.Settings()
        self.setMinimumWidth(self.settings.dock_min_width)
        self.adjustSize()
        
    def newProject(self, name):
        '''
        :Description:
            Called by DBus to manage the Project View Tree Widget
            
        :Returns:
            - name: string; The name of the Project to add to Widget
        '''
        return self.qctproject.newProject(name)

    def initTestData():
        pass