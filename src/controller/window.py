'''
Window Controller
'''

import model as m
import view.window as vw

class Window:
    
    @staticmethod
    def init():
        model = m.model(__name__)
        win = vw.Window()
        print(win) # FIXME: config and show window