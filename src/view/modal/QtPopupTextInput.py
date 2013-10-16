'''
:Description:
    This class represents a Qt Window that requests a single line
    of text. 
    
    Example: When creating a new project, you are prompted for the
             project name.
             
             
:Developers Note:
    Do not open up a prompt window for saving to a filesystem location.
    The more prompts a user has to endure, the more context switching
    and distractions are created. When the user wants to save, they
    will be prompted for a location; until then, it will be placed
    into temp folder (or a specified temporary folder) under a uuid
    or similar.
'''