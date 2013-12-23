from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import os

class AddCompilerAction():
    
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            # Initialize graphical elements, NOT callbacks as that is done
            # by the calling program through kwargs
            cls._instance = super(AddCompilerAction, cls).__new__(cls)
            # FIXME: cls.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, ''))
            #cls.qaction = QtGui.QAction(cls.qicon, '&Configuration', None)
            #cls.qaction.setStatusTip('&Add Compiler')
            #cls.qaction.triggered.connect(cls.add_compiler)
        return cls._instance

    @QtCore.pyqtSlot()
    def add_compiler():
        print("TODO popup window to add a compiler")