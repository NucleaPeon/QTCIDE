'''
Project Model

:Description:
    This project model is not a barebones model. It contains all the
    functionality for handling projects and data is saved in the
    cache

TODO: 
    - Validate that name is unique upon 
        a) rename of project
        b) new project
        
'''

PROJECT_FILTER = 'QTIDE Project (*.qtp)'

import os

class Project:
    
    name = None
    icon = None
    languages_used = []
    saved = False
    path = os.environ.get("HOME")
    filename = '' # If empty, must request SaveAs as opposed to Save