#exitAction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                            #'system-shutdown.png')), 
                                                #'&Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit Application')
        #exitAction.triggered.connect(QtGui.qApp.quit)
        
from PyQt4 import QtGui
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os        

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class ExitAction():
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(ExitAction, cls).__new__(cls)
            cls.qaction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'system-shutdown.png')),
                                        '&Exit', None)
            cls.qaction.setShortcut('Ctrl-Q')
            cls.qaction.setStatusTip('Exit Application')
            cls.qaction.triggered.connect(QtGui.qApp.quit)
        return cls._instance
