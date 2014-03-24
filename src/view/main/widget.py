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
        self.layout.addWidget(Selection())
        self.layout.addWidget(DropCanvas())
        
        self.code = CodeView()
        self.addTab(self.dnd, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'debug-step-out.png')), "Drag 'N Drop")
        self.addTab(self.code, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'view-calendar-journal.png')), "Code")
        
        
class Selection(QtGui.QGroupBox):
    
    def __init__(self):
        super(Selection, self).__init__()
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.setLayout(self.layout)
        self.pixmap = QtGui.QPixmap(os.path.join(SYS_IMG_FOLDER, 
                                             'folder-development.png'))
        # FIXME: Set text and image data for ALL mimetype objects
        # TODO: Objects need to be placed into a Scroll Pane
        self.newfile = Droppable()
        self.newfile.mime.setText("File")
        self.newfile.mime.setImageData(self.pixmap)
        self.newfile.setPixmap(self.pixmap)
        
        self.namespace = Droppable()
        self.namespace.mime.setText("Namespace")
        self.namespace.mime.setImageData(self.pixmap)
        self.namespace.setPixmap(self.pixmap)
        #self.namespace.setIconSize(QtCore.QSize(48, 48))
        
        self.classes = Droppable()
        self.classes.mime.setText("Class")
        self.classes.mime.setImageData(self.pixmap)
        self.classes.setPixmap(self.pixmap)
        
        self.function = Droppable()
        self.function.mime.setText("Function")
        self.function.mime.setImageData(self.pixmap)
        self.function.setPixmap(self.pixmap)
        self.variable = Droppable()
        self.variable.mime.setText("Variable")
        self.variable.mime.setImageData(self.pixmap)
        self.variable.setPixmap(self.pixmap)
        
        self.layout.addWidget(self.newfile)
        self.layout.addWidget(self.namespace)
        self.layout.addWidget(self.classes)
        self.layout.addWidget(self.function)
        self.layout.addWidget(self.variable)
        self.layout.insertStretch(-1)
        
        
class Droppable(QtGui.QLabel):
    
    def __init__(self):
        super(Droppable, self).__init__()
        self.mime = QtCore.QMimeData()
        ''' FIXME
        In order to prevent over abundance of copies and sets
        that are useless, perhaps have each object (such as Class or Function)
        in its own class that inherits this one and defines required information
        that can be set.
        
        Example: Namespace(Droppable) 
            - Contains variable self.text which is assigned to mimetype text()
            - Contains image which is assigned via setImageData
            
        This should not be done outside of this ,or similar, classes
        '''
        
    def mousePressEvent(self, event):
        mime = QtCore.QMimeData()
        mime.setText(self.mime.text())
        hotSpot = event.pos()
        mime.setData("application/x-hotspot", str(hotSpot.x()))
        
        # Create a pixmap of size of self
        pixmap = QtGui.QPixmap(self.size())
        self.render(pixmap)
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime)
        drag.setPixmap(pixmap)
        drag.setHotSpot(hotSpot)
        
        dropAction = drag.exec_(QtCore.Qt.CopyAction|QtCore.Qt.MoveAction, QtCore.Qt.CopyAction)
        #if dropAction == QtCore.Qt.MoveAction:
            #print("Do something")
        
        
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
                self.projects.project.addProject(proj)
                # leave as selected # Select and sort should be a macro TODO
                qmindex = self.projects.project.index(0, 0)
                self.projects.project.projecttree.setCurrentIndex(qmindex)
                self.projects.project.sort(0)
        
        
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
        self.layout.addWidget(QtGui.QLabel("Code View"))
        self.setLayout(self.layout)