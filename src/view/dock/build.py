from PyQt4 import QtGui, QtCore
import model.build
import view.actions.project.build.build 
import view.actions.project.build.configuration 

class Build(QtGui.QDockWidget):
    
    def __init__(self, *args, **kwargs):
        super(Build, self).__init__(**kwargs)
        self.widget = QtGui.QWidget()
        self.filemap = QtGui.QListView()
        self.filemodel = QtGui.QStandardItemModel()
        self.systems = QtGui.QStandardItemModel()
        self.filemap.setModel(self.filemodel)
        self.buildmodel = model.build.Build()
        self.populate()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Build Options", None, QtGui.QApplication.UnicodeUTF8))

        self.layout = QtGui.QVBoxLayout()
        self.grouplayout = QtGui.QVBoxLayout()
        
        self.group = QtGui.QGroupBox("Build Systems")
        self.buildbox = QtGui.QComboBox()
        # Add actions to kwargs
        kwargs['view.actions.project.build.build'] = view.actions.project.build.build.BuildSystemBuildAction()
        kwargs['view.actions.project.build.configuration'] = view.actions.project.build.configuration.BuildSystemConfigurationAction()
        self.buildconfig = QtGui.QPushButton(kwargs['view.actions.project.build.configuration'].qicon, "&Configure")
        self.buildbutton = QtGui.QPushButton(kwargs['view.actions.project.build.build'].qicon, "&Build")
        self.buildbox.setModel(self.systems)
        print(kwargs)
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
    def populate(self):
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