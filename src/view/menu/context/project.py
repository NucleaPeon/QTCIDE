from PyQt4 import QtGui, QtCore
import view.actions.project.new
import view.actions.project.close

'''
Project Contextual Menu, Right-Click on Project TreeView

When instantiated it will connect with the model.project
treeview component
'''
class ProjectContextMenu(QtGui.QMenu):

    
    def __init__(self, menu_items, *args, **kwargs):
        '''
        :Parameters:
            - menu_items: array of QAction references to add to the menu
            - **kwargs:
                - 'project': Project Dock instance
        '''
        super(ProjectContextMenu, self).__init__()
        for item in menu_items:
            self.addAction(item)
            print(item)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        self.popup(QtGui.QCursor.pos())
        
        