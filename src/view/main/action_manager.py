'''
Action Manager holds references to icons and their actions

:Description:
    In order to ensure only once instance of critical components exists at a time,
    a manager class (or factory) produces an instance of an object, yet 
    if additional requests are made to produce an object that already exists,
    its existing reference is returned instead.
    
    Unfortunately, Managers will be in Singleton form, but this means that
    all similar components can be accessed easily from one module and
    conveniences can be written in to improve accessibility and readability.
    
    In this class, all actions are instantiated here.
    Collections of actions are assigned into arrays so custom
    contextual menus can be produced with existing items.
'''

import view.actions.exit
import view.actions.project.close
import view.actions.project.new
import view.actions.project.save
import view.actions.project.settings
import view.actions.project.build.build
import view.actions.project.build.configuration
import view.actions.project.run.addrun
import view.actions.project.run.configurerun
import view.actions.project.run.removerun
import view.actions.project.testing.addsuite
import view.actions.project.testing.configurerun
import view.actions.project.testing.removesuite

class ActionManager():
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if _instance is None:
            cls._instance = super(ActionManager, cls).__new__(cls)
            # Define class attributes here
            cls.actions = {}
            
        return cls._instance
    
    
    def __init__(self, *args, **kwargs):
        pass