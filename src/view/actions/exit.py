from PyQt4 import QtGui
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os        

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class ExitAction(QtGui.QAction):
    
    def __init__(self):
        super(ExitAction, self).__init__(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'system-shutdown.png')),
                                    '&Exit', None)
        self.setShortcut('Ctrl-Q')
        self.setStatusTip('Exit Application')
        self.triggered.connect(QtGui.qApp.quit)
