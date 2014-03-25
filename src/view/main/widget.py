from PyQt4 import QtGui, QtCore
import os, copy
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import model.scene
import model.project
import view.main.dock_manager
'''
Integrated Shell is a widget that contains other widgets that act
on the desired programming language for drag and drop functionality.

Shell is a QTabWidget because both drag and drop and code view are
mutually exclusive and it allows for additional views.
'''
class IntegratedShell(QtGui.QTabWidget):
    
    def __init__(self, *args, **kwargs):
        super(IntegratedShell, self).__init__(*args)
        self.layout = QtGui.QHBoxLayout()
        
        ### 
        ### Method to determine how to load individual tabs
        ###
        self.dnd = QtGui.QWidget()
        self.dnd.setLayout(self.layout)
        self.languagedock = view.main.dock_manager.DockManager().LANGUAGE_DOCK
        self.languagedock.setMaximumWidth(320)
        self.layout.addWidget(self.languagedock)
        self.layout.addWidget(DropCanvas())
        self.code = CodeView()
        self.addTab(self.dnd, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'debug-step-out.png')), "Drag 'N Drop")
        self.addTab(self.code, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'view-calendar-journal.png')), "Code")
        
class DropCanvas(QtGui.QGraphicsView):
    
    def __init__(self, *args, **kwargs):
        '''
        :Description:
            QGraphicsView that takes droppable components
            
        :Parameters:
            - **kwargs: 
                - 'parent': (optional)  
        '''
        super(DropCanvas, self).__init__()
        self.projects = view.main.dock_manager.DockManager().PROJECT_DOCK
        self.setAcceptDrops(True)
        self.scene = model.scene.ProjectScene()
        
        
    #def mouseReleasedEvent(self, event):
        #print("released on {}".format(event.mimeData().text()))
        
    def dropEvent(self, event):
        '''
        :Description:
            Add a new project if 
        '''
        # Check selection: if no items in project model, add new one
        if not self.projects is None:
            if self.projects.project.rowCount() < 1:
                #TODO: Turn into a macro
                proj = model.project.Project()
                proj.name = "Untitled"# FIXME: Get unused project name
                self.projects.add_project_to_view(proj)
                self.projects.select_project()
        
    def dragEnterEvent(self, event):
        event.accept()
        
        
class CanvasItem(QtGui.QStandardItem):
    
    def __init__(self, *args, **kwargs):
        super(CanvasItem, self).__init__(*args)
        self.setEditable(False)
        
        
class CodeView(QtGui.QWidget):
    
    def __init__(self):
        super(CodeView, self).__init__()
        self.layout = QtGui.QGridLayout()
        self.codeview = QtGui.QPlainTextEdit()
        self.codefont = QtGui.QFont("Monospace", 10)
        self.codefont.setStyleHint(QtGui.QFont.TypeWriter)
        self.codeview.setFont(self.codefont)
        self.codeview.setReadOnly(True)
        self.codeview.setPlainText("Code View")
        self.layout.addWidget(self.codeview)
        self.setLayout(self.layout)
        