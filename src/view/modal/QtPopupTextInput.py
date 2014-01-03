'''
TODO: This dialog should reflect QtPopupConfirm, both should be converted
      to singletons and every call reassign parent/title/question/success/
      and failure parameters.

:Description:
    This class represents a Qt Window that requests a single line
    of text. 
    
    Example: When creating a new project, you are prompted for the
             project name.
             
             
:Developers Note:
    Do not open up a prompt window for saving to a filesystem location.
    The more prompts a user has to endure, the more context switching
    and distractions are created. When the user wants to save, they
    will be prompted for a location; until then, it will be placed
    into temp folder (or a specified temporary folder) under a uuid
    or similar.
'''
import sys
from PyQt4 import QtGui, QtCore

class QTextInputPopup(QtGui.QDialog):
    
    _instance = None
    def __new__(cls, title, label):
        if not cls._instance:
            cls._instance = super(QTextInputPopup, cls).__new__(cls)
            cls.textline = QtGui.QLineEdit()
            cls.textline.setFocus(True)
            cls.buttonBox = QtGui.QDialogButtonBox()
            cls.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            cls.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
            cls.buttonBox.accepted.connect(cls.accept)
            cls.buttonBox.rejected.connect(cls.reject)
            
        return cls._instance
            
    def __init__(self, title, label):
        super(QTextInputPopup, self).__init__()
        self.textline.clear()
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(QtGui.QLabel(label))
        self.layout.addWidget(self.textline)
        
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
            
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)

    def success(self, call):
        '''
        :Description:
            Add a callable method when OK is clicked
        '''
        if not call is None and callable(call):
            self.buttonBox.accepted.connect(call)
    
    def failure(self, call):
        '''
        :Description:
            Add a callable method when Cancel is clicked
        '''
        if not call is None and callable(call):
            self.buttonBox.rejected.connect(call)