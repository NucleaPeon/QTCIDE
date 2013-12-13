#exitAction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                            #'system-shutdown.png')), 
                                                #'&Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit Application')
        #exitAction.triggered.connect(QtGui.qApp.quit)
        
from PyQt4 import QtGui
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os        

class ExitAction():
    
    def __init__(self):
        self.qaction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'system-shutdown.png')),
                                        '&Exit', None)
        self.qaction.setShortcut('Ctrl-Q')
        self.qaction.setStatusTip('Exit Application')
        self.qaction.triggered.connect(QtGui.qApp.quit)