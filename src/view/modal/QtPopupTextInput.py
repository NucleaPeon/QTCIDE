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
    
    def __init__(self, title, label, success=None, failure=None):
        super(QTextInputPopup, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        self.textline = QtGui.QLineEdit()
        self.layout.addWidget(QtGui.QLabel(label))
        self.layout.addWidget(self.textline)
        
        buttonBox = QtGui.QDialogButtonBox(self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        if not success is None and callable(success):
            buttonBox.accepted.connect(success)
            
        if not failure is None and callable(failure):
            buttonBox.rejected.connect(failure)
            
        self.layout.addWidget(buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)
        self.exec_()
