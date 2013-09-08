'''
'''
from PyQt4 import QtGui, QtCore, Qt
import mainwindow

class Pane(QtGui.QWidget):
    '''
    '''
    
    def __init__(self, **kwargs):
        super().__init__( None,
                         QtGui.QDockWidget.DockWidgetClosable())
        # print(QtGui.QDockWidget.DockWidgetClosable)

        print("Done")