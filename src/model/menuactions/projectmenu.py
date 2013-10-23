'''
:Description:
    ProjectMenu is a backend abstraction of a right click menu
    with both the menu item name and its callback when clicked.
    Because this is an abstraction class, it can be used to 
    create various front-end objects with the same functionality
    without relying on any one graphical component. 
    
    For example, the callback can be called via a button, checkbox,
    an __init__ method, or other forms of code manipulation
    
    Callback is based on the name attribute. 
    
    :See:
        - controller.project; module: for more details
    
'''

import importlib

class ProjectMenu():
    
    def __init__(self, name, *args, **kwargs):
        '''
        :Parameters:
            - kwargs; dict:
                - 'visible'; bool: If False, do not show item
        '''
        self.name = name
        self.callback = None
        self.display = bool(kwargs.get('visible', True))
        
    def __str__(self):
        return self.name.replace('_', ' ').title()
        
    def report(self):
        return "{} -> {} ({}), [{}] {{}}".format(name, callback, 
                                                 self.display, len(args),
                                                 len(kwargs.keys()))