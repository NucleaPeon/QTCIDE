from PyQt4 import QtGui
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os        

"""
Class that represents the QAction object with icon and
no parent in a singleton class
"""
class CloseProjectAction():
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(CloseProjectAction, cls).__new__(cls)
            cls.qaction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'document-close.png')),
                                        '&Close Project', None)
            cls.qaction.setShortcut('Ctrl-C')
            cls.qaction.setStatusTip('Close Project')
            cls.qaction.triggered.connect(print)
        return cls._instance
