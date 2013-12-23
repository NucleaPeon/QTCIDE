from PyQt4 import QtGui, QtCore
import model.build
import view.actions.project.build.build as build
import view.actions.project.build.configuration as config

class Build(QtGui.QDockWidget):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Build, self).__new__(
                self, *args, **kwargs)
            self.widget = QtGui.QWidget()
            self.buildmodel = model.build.Build()
            self.buildmodel.findBuildSystems()
        return self._instance
    
    def __init__(self):
        super(Build, self).__init__()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Build Options", None, QtGui.QApplication.UnicodeUTF8))

        self.layout = QtGui.QVBoxLayout()
        self.grouplayout = QtGui.QVBoxLayout()
        
        self.group = QtGui.QGroupBox("Build Systems")
        self.buildbox = QtGui.QComboBox()
        self.buildconfig = QtGui.QPushButton(config.BuildSystemConfigurationAction().qicon, "&Configure")
        self.buildbutton = QtGui.QPushButton(build.BuildSystemBuildAction().qicon, "&Build")
        self.buildbox.setModel(self.buildmodel.systems)
        
        self.group.setLayout(self.grouplayout)
        self.grouplayout.addWidget(self.buildbox)
        self.grouplayout.addWidget(self.buildconfig)
        self.grouplayout.addWidget(self.buildbutton)
        self.layout.addWidget(self.group)
        
        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)