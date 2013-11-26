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
        self.icon = kwargs.get('icon')
        
    def save(self):
        '''
        :Description:
            Method to persist the Project and all dependent data to disk
            TODO: Implement
        '''
        return
        
    def __str__(self):
        try:
            import yaml
            return yaml.dump(self)
        except:
            return self.name