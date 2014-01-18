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
        
        
class Selection(QtGui.QWidget):
    
    def __init__(self):
        super(Selection, self).__init__()
        
        
class DropCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(DropCanvas, self).__init__()
        
class CodeView(QtGui.QWidget):
    
    def __init__(self):
        super(CodeView, self).__init__()
        self.layout = QtGui.QGridLayout()
        self.layout.addWidget(QtGui.QLabel("Code View"))
        self.setLayout(self.layout)