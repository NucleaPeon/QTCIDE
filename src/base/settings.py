'''
Settings Class

:Description:
    Contains a file that sets up default configurations or allows an override
    based on a .conf file;
    
    On linux, this might be in a folder called /etc/qtcide/settings.conf for 
    example. This file will dictate such things as startup dimensions (full
    screen for tablets), default behaviours for things such as asking to 
    save the project if changes have been made - or auto save, or auto discard
    changes, etc. etc.
    
    This file will automatically default to the most SANE and Protective 
    settings so you do not lose information and are aided until you (the user)
    can become powerful enough to adapt the program to your behaviours.
'''

# TODO: Configuration file override 

class Settings():
    
    _instance = None
    
    ### Dimension Customization ###
    
    ## custom_dimensions:
    ## - True: Use x, y, width and height to set up window
    ## - False: Allow OS to determine dimensions
    custom_dimensions = False
    ## fullscreen:
    ## - True: Ignore x, y, width and height to use maximum screen real estate
    ##         Does not apply if custom_dimensions is set to False.
    ## - False: Abide by custom dimension settings.
    fullscreen = False
    
    x = 200
    y = 200
    width = 1000
    height = 600
    
    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Settings, self).__new__(
                self, *args, **kwargs)
        return self._instance
        
        
    
