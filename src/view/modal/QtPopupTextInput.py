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
import sys
from PyQt4 import QtGui

def getTextPopup(parent, title, question, callback=None):
    '''
    :Description:
        A popup that requests the user input text. Has an OK and Cancel
        button, when OK is clicked, input text is sent to the callback
        as the first parameter.
        
    :Parameters:
        - parent; QWidget: Because this method isn't in a class that is
          a widget, it requires a Widget to display itself (in a qt exec loop)
          so the calling QWidget should put "self" for that attribute.
        - title; string: Title of popup window
        - question; string: What to ask the user
        - callback; callable object, method: On OK, send result to this 
          method
    '''
    text, ok = QtGui.QInputDialog.getText(parent, title, 
        question)
        
    if ok:
        callback("{}".format(text))