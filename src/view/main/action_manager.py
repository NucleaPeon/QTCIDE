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
import view.actions.project.build.new
import view.actions.project.build.configure
import view.actions.project.run.new
import view.actions.project.run.configure
import view.actions.project.run.remove
import view.actions.project.testing.new
import view.actions.project.testing.configure
import view.actions.project.testing.remove

class ActionManager():
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ActionManager, cls).__new__(cls)
            # Define easy access constant variables here:
            cls.PROGRAM_EXIT = view.actions.exit.ExitAction()
            cls.PROJECT_NEW = view.actions.project.new.NewProjectAction()
            cls.PROJECT_CLOSE = view.actions.project.close.CloseProjectAction()
            cls.PROJECT_SAVE = view.actions.project.save.SaveProjectAction()
            cls.PROJECT_SETTINGS = view.actions.project.settings.ProjectSettingsAction()
            cls.BUILD_NEW = view.actions.project.build.new.NewBuildSystemBuildAction()
            cls.BUILD_CONFIG = view.actions.project.build.configure.BuildSystemConfigurationAction()
            cls.RUN_NEW = view.actions.project.run.new.NewRunAction()
            cls.RUN_CONFIG = view.actions.project.run.configure.ConfigureRunAction()
            cls.RUN_REMOVE = view.actions.project.run.remove.RemoveRunAction()
            cls.TEST_NEW = view.actions.project.testing.new.NewTestSuiteAction()
            cls.TEST_CONFIG = view.actions.project.testing.configure.ConfigureTestSuiteAction()
            cls.TEST_REMOVE = view.actions.project.testing.remove.RemoveTestSuiteAction()
            
            # Define class attributes here
            '''
            It is recommended to use this dictionary for retrieving a list
            of actions (ex: all project.* actions) or when adding your own
            menu actions to the IDE. As well, it is more readable to use
            dict.get(value, default_value) instead of checking for None, then
            re-assigning.
            '''
            cls.ACTIONS = {'exit': cls.PROGRAM_EXIT,
                           'project.new': cls.PROJECT_NEW,
                           'project.close': cls.PROJECT_CLOSE,
                           'project.save': cls.PROJECT_SAVE,
                           'project.settings': cls.PROJECT_SETTINGS,
                           'build.new': cls.BUILD_NEW,
                           'build.config': cls.BUILD_CONFIG,
                           'run.new': cls.RUN_NEW,
                           'run.config': cls.RUN_CONFIG,
                           'test.new': cls.TEST_NEW,
                           'test.config': cls.TEST_CONFIG,
                           'test.remove': cls.TEST_REMOVE}

        return cls._instance
    
    
    def __init__(self, *args, **kwargs):
        pass