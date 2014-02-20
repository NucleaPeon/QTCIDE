from PyQt4 import QtGui, QtCore

"""
Pane that inherits QStandardItemModel and contains information
on the User Interface components that it is associated with.

:Description:
    When the user navigates the Project Settings, it contains a left
    hand navigation list with graphical components that get set on
    the right.
    
    This class defines the text (and icon) which get set on the left,
    while also containing the graphical components on the right.
    
    This is done by writing the __left__() and __right__() methods
    in any class that inherits this one.
    
    If this class is inherited and methods are not filled out, the
    item will appear but will be blank.
    
"""

class ProjectSettingsPane(QtGui.QStandardItem):
    
    def __init__(self, *args, **kwargs):
        super(ProjectSettingsPane, self).__init__()
    
    
    def __left__(self):
        print("left")
    
    def __right__(self):
        print("right")
    