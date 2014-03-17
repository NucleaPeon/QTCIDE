from PyQt4 import QtGui, QtCore
import model.build
import view.actions.project.build.build as build
import view.actions.project.build.configuration as config

class Build(QtGui.QDockWidget):
    
    def __init__(self, *args, **kwargs):
        super(Build, self).__init__(**kwargs)
        self.widget = QtGui.QWidget()
        self.filemap = QtGui.QListView()
        self.filemodel = QtGui.QStandardItemModel()
        self.systems = QtGui.QStandardItemModel()
        self.filemap.setModel(self.filemodel)
        self.buildmodel = model.build.Build()
        self.findBuildSystems()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Build Options", None, QtGui.QApplication.UnicodeUTF8))

        self.layout = QtGui.QVBoxLayout()
        self.grouplayout = QtGui.QVBoxLayout()
        
        self.group = QtGui.QGroupBox("Build Systems")
        self.buildbox = QtGui.QComboBox()
        self.buildconfig = QtGui.QPushButton(config.BuildSystemConfigurationAction().qicon, "&Configure")
        self.buildbutton = QtGui.QPushButton(build.BuildSystemBuildAction().qicon, "&Build")
        self.buildbox.setModel(self.systems)
        
        self.group.setLayout(self.grouplayout)
        self.grouplayout.addWidget(self.buildbox)
        self.grouplayout.addWidget(self.buildconfig)
        self.grouplayout.addWidget(self.buildbutton)
        #self.grouplayout.addWidget(self.filemap)
        self.layout.addWidget(self.group)
        self.layout.insertStretch(-1)
        
        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)
        
    #FIXME: Move to view build component
    def findBuildSystems(self):
        '''
        :Description:
            Clears and adds all found build systems into the model
            
            Build systems are attached to the IDE by configuration
            files. Project settings window will allow for users to 
            find their own build system.
            
        '''
        # FIXME: At Milestone 5
        for sys in ['<none>', 'cmake', 'automake', 'make', 'qmake']:
            self.systems.appendRow(QtGui.QStandardItem(sys))