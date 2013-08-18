'''
'''
from PyQt4 import QtGui, QtCore, Qt
import mainwindow

class Pane(QtGui.QDockWidget):
    '''
    '''
    
    def __init__(self, **kwargs):
        super().__init__('Empty Pane', parent=kwargs.get('parent', None),
                         flags=) #FIXME
        # print(QtGui.QDockWidget.DockWidgetClosable)

        print("Done")