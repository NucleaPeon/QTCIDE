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
    
    init = {'QtGui.QApplication.translate': ["C and C++ Development Environment", 
                                             "C and C++ Development Environment", 
                                             None, QtGui.QApplication.UnicodeUTF8]}
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Window, self).__new__(
                self, *args, **kwargs)
            # initialize triggers here
        return self._instance
    
    def __init__(self):
        pass