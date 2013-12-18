from PyQt4 import QtGui, QtCore

class Build:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Build, self).__new__(
                self, *args, **kwargs)
            self.systems = QtGui.QStandardItemModel() # Project data
        return self._instance
    
    def findBuildSystems(self):
        '''
        :Description:
            Clears and adds all found build systems into the model
            
            Build systems are attached to the IDE by configuration
            files. Project settings window will allow for users to 
            find their own build system.
            
        '''
        # FIXME: At Milestone 5
        for sys in ['<none>', 'cmake', 'automake', 'make']:
            self.systems.appendRow(QtGui.QStandardItem(sys))