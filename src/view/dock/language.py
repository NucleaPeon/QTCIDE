'''
'''

from PyQt4 import QtGui, QtCore


class Language(QtGui.QDockWidget):
    
    def __init__(self, *args, **kwargs):
        super(Language, self).__init__()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        
        
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