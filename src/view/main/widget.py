from PyQt4 import QtGui, QtCore
import os
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON

'''
Integrated Shell is a widget that contains other widgets that act
on the desired programming language for drag and drop functionality.

Shell is a QTabWidget because both drag and drop and code view are
mutually exclusive and it allows for additional views.
'''
class IntegratedShell(QtGui.QTabWidget):
    
    def __init__(self):
        super(IntegratedShell, self).__init__()
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
        self.namespace = QtGui.QLabel()
        self.namedrag = QtGui.QDrag(self.namespace)
        self.namemime = QtCore.QMimeData()
        self.namemime.setText("Namespace")
        self.namemime.setImageData(self.pixmap)
        
        self.namespace.setPixmap(self.pixmap)
        #self.namespace.setIconSize(QtCore.QSize(48, 48))
        self.classes = QtGui.QLabel()
        self.classesdrag = QtGui.QDrag(self.classes)
        self.classesmime = QtCore.QMimeData()
        self.classes.setPixmap(self.pixmap)
        self.function = QtGui.QLabel()
        self.functiondrag = QtGui.QDrag(self.function)
        self.functionmime = QtCore.QMimeData()
        self.function.setPixmap(self.pixmap)
        self.variable = QtGui.QLabel()
        self.variabledrag = QtGui.QDrag(self.variable)
        self.variablemime = QtCore.QMimeData()
        self.variable.setPixmap(self.pixmap)
        
        self.layout.addWidget(self.namespace)
        self.layout.addWidget(self.classes)
        self.layout.addWidget(self.function)
        self.layout.addWidget(self.variable)
        self.layout.insertStretch(-1)
        
        
        
        
class DropCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(DropCanvas, self).__init__()
        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)
        self.canvas = QtGui.QListView()
        self.layout.addWidget(self.canvas)
        self.setAcceptDrops(True)
        
class CodeView(QtGui.QWidget):
    
    def __init__(self):
        super(CodeView, self).__init__()
        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(QtGui.QLabel("Code View"))
        self.setLayout(self.layout)