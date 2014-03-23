import view.main.action_manager as actions

class MenuBar:
    
    '''
    :Description:
        Expects the mainwindow to pass in its menubar object.
        Configures the menubar with the appropriate menus
        by importing and adding all actions.
        
    :Parameters:
        - mainwindow: PyQt4 QMainWindow object reference
    '''
    def __init__(self, mainwindow, *args, **kwargs):
        # Instantiate Menu components here
        self.mgr_actions = actions.ActionManager()
        self.mwin = mainwindow
        self.menubar = self.mwin.menuBar()
        
        # File Menu
        self.filemenu = self.menubar.addMenu('&File')
        self.filemenu.addAction(self.mgr_actions.PROGRAM_EXIT)
        # View Menu
        self.viewMenu = self.menubar.addMenu('&View')
        # View -> Dock Sub Menu
        self.viewDockMenu = self.viewMenu.addMenu('&Docks')
        
        # Project Menu
        self.projMenu = self.menubar.addMenu('&Project')
        self.projMenu.addAction(self.mgr_actions.PROJECT_NEW)
        self.projMenu.addAction(self.mgr_actions.PROJECT_SAVE)
        self.projMenu.addAction(self.mgr_actions.PROJECT_CLOSE)
        self.projMenu.addAction(self.mgr_actions.PROJECT_SETTINGS)
        self.projBuildMenu = self.projMenu.addMenu('&Build')
        self.projBuildMenu.addAction(self.mgr_actions.BUILD_NEW)
        self.projBuildMenu.addAction(self.mgr_actions.BUILD_CONFIG)
        self.projRun = self.projMenu.addMenu('&Run')
        self.projRun.addAction(self.mgr_actions.RUN_NEW)
        self.projRun.addAction(self.mgr_actions.RUN_CONFIG)
        self.projRun.addAction(self.mgr_actions.RUN_REMOVE)
        self.projTest = self.projMenu.addMenu('&Test')
        self.projTest.addAction(self.mgr_actions.TEST_NEW)
        self.projTest.addAction(self.mgr_actions.TEST_CONFIG)
        self.projTest.addAction(self.mgr_actions.TEST_REMOVE)
        
        
        # Help Menu
        self.helpMenu = self.menubar.addMenu('&Help')
        
        # Toolbar
        self.filetb = self.mwin.addToolBar('File')
        self.filetb.addAction(self.mgr_actions.PROGRAM_EXIT)
        self.projtb = self.mwin.addToolBar('Project')
        self.projtb.addAction(self.mgr_actions.PROJECT_NEW)
        self.projtb.addAction(self.mgr_actions.PROJECT_CLOSE)
        self.projtb.addAction(self.mgr_actions.PROJECT_SAVE)
        self.projtb.addAction(self.mgr_actions.PROJECT_SETTINGS)
        self.buildtb = self.mwin.addToolBar('Build')
        self.buildtb.addAction(self.mgr_actions.BUILD_NEW)
        self.buildtb.addAction(self.mgr_actions.BUILD_CONFIG)
        self.runtb = self.mwin.addToolBar('Run')
        self.runtb.addAction(self.mgr_actions.RUN_NEW)
        self.testtb = self.mwin.addToolBar('Test')
        self.testtb.addAction(self.mgr_actions.TEST_NEW)
        self.testtb.addAction(self.mgr_actions.TEST_CONFIG)
        self.testtb.addAction(self.mgr_actions.TEST_REMOVE)
        self.runtb.addAction(self.mgr_actions.RUN_NEW)
        self.runtb.addAction(self.mgr_actions.RUN_CONFIG)
        self.runtb.addAction(self.mgr_actions.RUN_REMOVE)
        
        