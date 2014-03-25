'''
'''

from PyQt4 import QtGui, QtCore
import os
from view.img import SYS_IMG_FOLDER


class Language(QtGui.QDockWidget):
    
    def __init__(self, *args, **kwargs):
        super(Language, self).__init__()
        # TODO: Is dock movable in xp/7/osx? On Gentoo Linux it currently isn't,
        # See here: http://python.6.x6.nabble.com/QDockWidget-issue-in-Linux-but-not-Windows-OSX-td4374122.html
        self.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|
                         QtGui.QDockWidget.DockWidgetMovable)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.selection = self.Selection()
        self.widget = QtGui.QWidget()
        self.layout = QtGui.QVBoxLayout()
        self.langlayout = QtGui.QHBoxLayout(self.widget)
        self.languagewidget = QtGui.QWidget(self.widget)
        self.languagewidget.setLayout(self.langlayout)
        self.widget.setLayout(self.layout)
        self.languagebox = QtGui.QComboBox(self.languagewidget)
        self.languagebox.addItem("C++")
        self.languagebox.addItem("Java")
        self.languagebox.addItem("Python")
        self.languagebox.addItem("")
        self.languagebox.addItem("Add Language...")
        self.langlayout.addWidget(QtGui.QLabel("Language:"))
        self.langlayout.addWidget(self.languagebox)
        self.langlayout.addStretch()
        self.layout.addWidget(self.languagewidget)
        self.layout.addWidget(self.selection)
        self.setWidget(self.widget)
        
        
        
    class Selection(QtGui.QGroupBox):
        
        def __init__(self):
            super(Language.Selection, self).__init__()
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
            