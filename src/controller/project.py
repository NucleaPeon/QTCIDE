'''
ProjectController - Handles menu action registrations for Project Menus
'''


'''
:Description:
    Dictionary that contains a list of names in a specific format:
        - {"lower_case_description": binary_flag, 
           "another_menu_maybe": binary_flag}
           
    Do not worry about binary flag, that is used for specifying multiple
    actions in a menu using AND/OR, but since it's in a dictionary, IDE's
    can autocomplete using names and by using names, it becomes more
    self-explanatory what the code is doing.
    
    The dictionary key is special in that when the value is initialized into a 
    ProjectMenu object (or any other _____Menu() object), it does 
    two things: 
        # Converts _ to " " (spaces) when creating the menu item name,
            string is split on spaces and each word is capitalized
            - Example: "Lower Case Description" is the menu item name
        # Callback is immediately associated to a method of the same
            value as the format. 
            - Example: "Lower Case Description" -> will look for a method
                in the object called "self.lower_case_description()"
                
    This complexity removes the need for hardcoding menu items and actions
    together. As long as the list is ordered as desired by the developer,
    it should appear without issue.
    
:Developer's Note:
    Because Singleton patterns are not recommended, the use of a module
    (which is essentially a singleton pattern) is more appropriate for
    controllers.
'''

import model.project as projmodel
PROJECTS = {}
    
def initialize_project(name, *args, **kwargs):
    '''
    :Description:
        Invokes all neccessary startup sequences required for a default
        template empty project to be created and available to the user
        through backend configuration. Frontend configuration should be
        done on project creation request (through menu or button) and
        set up applicable ui components -- it will not be done here.
        Note: Set up frontend after backend setup is complete
        
        There should be no disk usage to get the project started until
        a user requests a save.
    '''
    PROJECTS[name] = projmodel.Project(name, *args, **kwargs)
    return PROJECTS[name]