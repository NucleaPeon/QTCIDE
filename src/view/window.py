from PyQt4 import QtGui, QtCore

'''
Window View

Contains the visual content of the main window.

Only one window should exist at one time per instance. Other modal windows 
should use QDialogs. 
'''
class Window(QtGui.QMainWindow):
    
    def __init__(self):
        pass