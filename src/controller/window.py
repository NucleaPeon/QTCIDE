'''
Window Controller
'''

import controller as c
import view.window as vw

class Window:
    
    @staticmethod
    def init():
        model = c.model(__name__)
        win = vw.Window()
        print(win) # FIXME: config and show window