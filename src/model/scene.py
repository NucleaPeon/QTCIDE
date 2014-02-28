from PyQt4 import QtGui, QtCore

'''
This class represents the entire graphical scene that the user sees
for drag and drop.

Double click an item in the scene to display another window with 
more detailed contents of that scene object.
'''

class ProjectScene(QtGui.QGraphicsScene):
    
    def __init__(self, *args, **kwargs):
        super(ProjectScene, self).__init__(*args)