'''
:Description:
    ProjectMenu is a backend abstraction of a right click menu
    with both the menu item name and its callback when clicked.
    Because this is an abstraction class, it can be used to 
    create various front-end objects with the same functionality
    without relying on any one graphical component. 
    
    For example, the callback can be called via a button, checkbox,
    an __init__ method, or other forms of code manipulation
    
'''

class ProjectMenu():
    
    def __init__(self, name, callback, *args, **kwargs):
        self.name = name
        self.callback = callback
        
    def __str__(self):
        return "{} {}, [{}] {{}}".format(name, callback, len(args),
                                         len(kwargs.keys()))