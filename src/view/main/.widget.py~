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
        self.setLayout(self.layout)
        
        ### 
        ### Method to determine how to load individual tabs
        ###
        qw1 = QtGui.QWidget()
        qw2 = QtGui.QWidget()
        self.addTab(qw1, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'debug-step-out.png')), "Drag 'N Drop") # QWidget # 
        self.addTab(qw2, QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'view-calendar-journal.png'), "Code")) # QWidget
        
        
class Selection(QtGui.QWidget):
    
    def __init__(self):
        super(Selection, self).__init__()
        
        
class DropCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(DropCanvas, self).__init__()
        
class CodeView(QtGui.QWidget):
    
    def __init__(self):
        super(CodeView, self).__init__()