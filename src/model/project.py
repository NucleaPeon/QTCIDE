'''
:Description:
    Module that contains the model of a Project:
        - a collection of files, resources and configurations
        
:Depends:
    - python yaml plugin (optional)
    If yaml is not found, project str() returns the project name.
        
'''
from PyQt4 import QtGui

class Project:
    
    def __init__(self, name, *args, **kwargs):
        '''
        :Description:
            A project model; a representation of a project
            in the QT-C-IDE framework.
        '''
        self.name = name
        self.path = kwargs.get('path', None)
        self.model = QtGui.QStandardItemModel()
        
    def __str__(self):
        try:
            import yaml
            return yaml.dump(self)
        except:
            return self.name
        
def createNewProject(name):
    '''
    :Description:
        A factory class that returns an instantiated project model
        
    :Parameters:
        - name; string: Name of the project
    '''
    return Project(name)