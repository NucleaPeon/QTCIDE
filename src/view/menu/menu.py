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
        self.toolbar = self.mwin.addToolBar('File')
        # Cannot extend QWidget, so must access variable 
        self.exit_action = view.actions.exit.ExitAction().qaction
        self.toolbar.addAction(self.exit_action)