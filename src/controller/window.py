'''
Window Controller
'''

import controller as c

class Window:
    
    @staticmethod
    def init():
        model = c.model(__name__)
        print(model)