'''
Window Controller
'''

import view.window as vw

class Window:
    
    '''
    :Description:
        Instantiates (and returns) the main window.
        
        The window must be returned because a reference
        must always exist to the QMainWindow, otherwise the gc will
        dispose of your ui.
    '''
    @staticmethod
    def init():
        win = vw.Window()
        return win