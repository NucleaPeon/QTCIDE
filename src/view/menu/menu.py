import view.actions.exit
import view.actions.project.new
import view.actions.project.close
import view.actions.project.save
import view.actions.project.build.build
import view.actions.project.build.configuration
import view.actions.project.run.addrun
import view.actions.project.run.removerun
import view.actions.project.run.configurerun

class MenuBar:
    
    '''
    :Description:
        Expects the mainwindow to pass in its menubar object.
        Configures the menubar with the appropriate menus
        by importing and adding all actions.
        
    :Parameters:
        - mainwindow: PyQt4 QMainWindow object reference
    '''
    def __init__(self, mainwindow):
        # Instantiate Menu components here
        self.mwin = mainwindow
        self.menubar = self.mwin.menuBar()
        # Instantiate all actions here
        self.exit_action = view.actions.exit.ExitAction().qaction
        self.projNewAction = view.actions.project.new.NewProjectAction().qaction
        self.projCloseAction = view.actions.project.close.CloseProjectAction().qaction
        self.projSaveAction = view.actions.project.save.SaveProjectAction().qaction
        self.projBuild = view.actions.project.build.build.BuildSystemBuildAction().qaction
        self.projBuildConfig = view.actions.project.build.configuration.BuildSystemConfigurationAction().qaction
        self.projAddRun = view.actions.project.run.addrun.AddRunAction().qaction
        self.projRemRun = view.actions.project.run.removerun.RemoveRunAction().qaction
        self.projRunConfig = view.actions.project.run.configurerun.ConfigureRunAction().qaction
        
        # File Menu
        self.filemenu = self.menubar.addMenu('&File')
        self.filemenu.addAction(self.exit_action)
        # View Menu
        self.viewMenu = self.menubar.addMenu('&View')
        # View -> Dock Sub Menu
        self.viewDockMenu = self.viewMenu.addMenu('&Docks')
        
        # Project Menu
        self.projMenu = self.menubar.addMenu('&Project')
        self.projMenu.addAction(self.projNewAction)
        self.projMenu.addAction(self.projCloseAction)
        self.projBuildMenu = self.projMenu.addMenu('&Build')
        self.projBuildMenu.addAction(self.projBuild)
        self.projBuildMenu.addAction(self.projBuildConfig)
        self.projRun = self.projMenu.addMenu('&Run')
        self.projRun.addAction(self.projAddRun)
        self.projRun.addAction(self.projRemRun)
        self.projRun.addAction(self.projRunConfig)
        
        
        # Help Menu
        self.helpMenu = self.menubar.addMenu('&Help')
        
        # Toolbar
        self.filetb = self.mwin.addToolBar('File')
        self.filetb.addAction(self.exit_action)
        self.projtb = self.mwin.addToolBar('Project')
        self.projtb.addAction(self.projNewAction)
        self.projtb.addAction(self.projCloseAction)
        self.projtb.addAction(self.projSaveAction)
        self.buildtb = self.mwin.addToolBar('Build')
        self.buildtb.addAction(self.projBuild)
        self.buildtb.addAction(self.projBuildConfig)
        self.runtb = self.mwin.addToolBar('Run')
        self.runtb.addAction(self.projAddRun)
        self.runtb.addAction(self.projRemRun)
        self.runtb.addAction(self.projRunConfig)
        
        