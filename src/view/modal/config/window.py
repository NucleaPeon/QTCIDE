'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore

class ProjectConfiguration(QtGui.QWidget):
    
    def __init__(self):
        super(QtGui.QtWidget, self).__init__()