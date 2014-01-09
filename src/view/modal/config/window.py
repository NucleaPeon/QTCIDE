'''
The window, main layout and frame of the configuration modal
that is displayed. 

Configuration window displays other view.modal.config modules

'''

from PyQt4 import QtGui, QtCore

class ProjectConfiguration(QtGui.QDialog):
    
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ProjectConfiguration, cls).__new__(cls)
            cls.buttonBox = QtGui.QDialogButtonBox()
            cls.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            cls.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
            cls.buttonBox.accepted.connect(cls.accept)
            cls.buttonBox.rejected.connect(cls.reject)
            
        return cls._instance
    
    def __init__(self, title="Project Settings"):
        super(ProjectConfiguration, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        
        self.buttonBox.accepted.disconnect()
        self.buttonBox.rejected.disconnect()
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
            
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.setWindowTitle(title)
        
    