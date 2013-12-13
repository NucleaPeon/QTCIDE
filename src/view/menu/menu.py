import view.actions.exit

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
        self.mwin = mainwindow
        self.menubar = self.mwin.menuBar()
        self.exit_action = view.actions.exit.ExitAction().qaction
        # File Menu
        self.filemenu = self.menubar.addMenu('&File')
        self.filemenu.addAction(self.exit_action)
        # View Menu
        self.viewMenu = self.menubar.addMenu('&View')
        # Project Menu
        self.projMenu = self.menubar.addMenu('&Project')
        # Help Menu
        self.helpMenu = self.menubar.addMenu('&Help')
        
        # Toolbar
        self.toolbar = self.mwin.addToolBar('File')
        self.toolbar.addAction(self.exit_action)