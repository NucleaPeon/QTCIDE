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
    
    Defining the graphical component requires a method named
    "settings"
    
    Ex: 
        def settings(self, ...):
            return QWidget object
            
    You may want to store the widget's state in the class so it can be
    retrieved quickly, instead of recreating the widget and returning 
    it every method call.
    
"""

class ProjectSettingsPane(QtGui.QStandardItem):
    '''
    :Description:
        Base QStandardItem that controls Project Settings panes
        that appear in the modal window. Having dynamically loadable
        setting pane modules allows developers to add and remove
        setting options based on what python modules are detected.
        
        
    :Parameters:
        - *args: Expects the exact same parameters you would submit in
                 order to initialize a QStandardItem
                 
                 Ex: QString text,
                     QIcon icon, QString text
                     int rows, int columns = 1
                     QStandardItem other
            
          If none of the above values are submitted, a blank entry
          will exist in the project settings view.
    '''
    
    def __init__(self, *args, **kwargs):
        super(ProjectSettingsPane, self).__init__(*args)
    
    def settings(self):
        return QtGui.QLabel("This is ProjectSettingsPane")
    