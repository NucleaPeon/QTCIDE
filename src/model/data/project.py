'''
Model that contains an array of components that make up the Project
'''

import controller.project

import os

'''
:Description:
    The project data model is a storage class for all components of the project
    
    This includes data such as run configurations, test suites, build setup,
    and custom project information. 
'''
class ProjectData:
    
    
    FSYS = {'local': lambda: controller.project.persist('local', self)}
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', None)
        self.icon = kwargs.get('icon', None)
        self.save = kwargs.get('save', False)
        self.fsys = kwargs.get('fsys', self.FSYS.get('local'))
        self.path = kwargs.get('path', os.environ['HOME'])
        if self.name is None:
            raise Exception('Project has no filename')
        self.filename = kwargs.get('filename', '{}.{}'.format(self.name, 'qtc'))

        
        
    def save(self):
        controller.project.persist(self.fsys, self)