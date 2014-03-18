from PyQt4 import QtGui, QtCore
import view.components.project
import view.actions.project.new
import view.actions.project.close

'''
Project Contextual Menu, Right-Click on Project TreeView

When instantiated it will connect with the model.project
treeview component
'''
class ProjectContextMenu(QtGui.QMenu):

    
    def __init__(self, *args, **kwargs):
        '''
        :Parameters:
            - **kwargs:
                - 'project': Project Dock instance
        '''
        super(ProjectContextMenu, self).__init__()
        self.project = kwargs.get('project')
        self.new_project = view.actions.project.new.NewProjectAction()
        self.close_project = view.actions.project.close.CloseProjectAction()
        self.addAction(self.new_project)
        self.addAction(self.close_project)
    
    @QtCore.pyqtSlot(QtCore.QPoint)
    def displayProjectMenu(self, point):
        print("point {}".format(point))
        self.popup(QtGui.QCursor.pos())
        
        