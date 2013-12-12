from PyQt4 import QtGui
'''
Window Model

There are some attributes that when detected, are used automatically.

    - init = {}
        - every key in init dictionary is a method that is found in self,
          the value is an array of arguments.
'''
class Window:
    
    _instance = None
    
    ## custom_dimensions:
    ## - True: Use x, y, width and height to set up window
    ## - False: Allow OS to determine dimensions
    custom_dimensions = True
    ## fullscreen:
    ## - True: Ignore x, y, width and height to use maximum screen real estate
    ##         Does not apply if custom_dimensions is set to False.
    ## - False: Abide by custom dimension settings.
    fullscreen = False
    
    x = 100
    y = 100
    width = 1400
    height = 800
    
    dock_min_width = 300
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Window, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        pass
    
    # Singleton Window settings, such as dimensions FIXME