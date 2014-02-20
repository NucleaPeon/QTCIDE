from PyQt4 import QtGui, QtCore

'''
Basic project settings
'''

class Project(QtGui.QGroupBox):
    
    _instance = None # Single instance of initialized class
    
    _Name_ = """Project"""
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Project, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(Project, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        # Add __left__ components of objects