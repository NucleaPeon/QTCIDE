'''
:Description:
    This class represents a Qt Window that requests a Question
    with a label.
    
    Example: When removing a configuration file, prompt user and
             only perform removal on OK button
             
'''
import sys
from PyQt4 import QtGui, QtCore

class QtPopupConfirm(QtGui.QDialog):
    
    _instance = None
    def __new__(cls, title, label):
        if not cls._instance:
            cls._instance = super(QtPopupConfirm, cls).__new__(cls)
            cls.textline = QtGui.QLineEdit()
            cls.textline.setFocus(True)
            cls.buttonBox = QtGui.QDialogButtonBox()
            cls.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            cls.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
            cls.buttonBox.accepted.connect(cls.accept)
            cls.buttonBox.rejected.connect(cls.reject)
            
        return cls._instance
    
    def __init__(self, title, label):
        super(QtPopupConfirm, self).__init__()
        self.textline.clear()
        self.layout = QtGui.QVBoxLayout()
        self.lineedit = QtGui.QLineEdit()
        self.layout.addWidget(self.lineedit)
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