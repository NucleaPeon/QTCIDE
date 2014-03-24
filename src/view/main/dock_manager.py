'''
Dock Manager holds references to dock objects

:Description:
    In order to ensure only one instance of a dock exists at a time
    and can be referenced where required, this manager class will
    contain that reference and can be retrievable either using
    a dictionary or through manually set up variables that point
    to references.
    
    
'''

import view.dock.build
import view.dock.run
import view.dock.testing
import view.dock.terminal
import view.dock.project

class DockManager():
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DockManager, cls).__new__(cls)
            cls.BUILD_DOCK = view.dock.build.Build()
            cls.PROJECT_DOCK = view.dock.project.Project()
            cls.RUN_DOCK = view.dock.run.Run()
            cls.TERMINAL_DOCK = view.dock.terminal.Terminal()
            cls.TESTING_DOCK = view.dock.testing.Testing()
            cls.LANGUAGE_DOCK = None # TODO: Create and enable docking in center widget
            # May have to subclass dock and widget to allow only that widget to dock
            cls.DOCKS = {'build': cls.BUILD_DOCK,
                         'project': cls.PROJECT_DOCK,
                         'run': cls.RUN_DOCK,
                         'terminal': cls.TERMINAL_DOCK,
                         'testing': cls.TESTING_DOCK,
                         'language': cls.LANGUAGE_DOCK
                         }
        return cls._instance
    
    
    def __init__(self, *args, **kwargs):
        pass