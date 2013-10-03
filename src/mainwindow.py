#!/usr/bin/env python3
import os
from src.base.window import Window
from PyQt4 import QtGui, QtCore
import src.base.settings as s
from src.img import SYS_IMG_FOLDER, SYS_APP_ICON

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.settings = s.Settings()
        self.resize(self.settings.width, self.settings.height)
        self.setWindowTitle(QtGui.QApplication.translate("C and C++ Development Environment", 
                                                         "C and C++ Development Environment", 
                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = Window()
        self.centralwidget.hide()
        self.setCentralWidget(self.centralwidget) 
        
        self.setWindowIcon(QtGui.QIcon(SYS_APP_ICON))
        # X, Y, Width, Height
        #if s.custom_dimensions:
            #if s.fullscreen:
                #screen = QtGui.QDesktopWidget().screenGeometry()
                #self.setGeometry(0, 0, screen.width(), screen.height())
            #else:
                #self.setGeometry(s.x, s.y, s.width, s.height)
        
        
        self.dockProject = QtGui.QDockWidget(self)
        self.dockProject.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockProject.setWindowTitle(QtGui.QApplication.translate(
            "self", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.dockProjectContents = QtGui.QWidget()
        self.dockProject.setWidget(self.dockProjectContents)
        '''
        Qt::LeftDockWidgetArea  0x1
        Qt::RightDockWidgetArea 0x2
        Qt::TopDockWidgetArea   0x4
        Qt::BottomDockWidgetArea        0x8
        Qt::AllDockWidgetAreas  DockWidgetArea_Mask
        Qt::NoDockWidgetArea    0
        '''
        self.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockProject)
        
        # Set Statusbar message (included in MainWindow)
        self.status("Ready")
        
        # Actions
        
        exitAction = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                            'system-shutdown.png')), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        newProject = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                            'document-new.png')), '&New Project', self)
        newProject.setShortcut('Ctrl+N')
        newProject.setStatusTip('New Project')
        
        preferenceWin = QtGui.QAction(QtGui.QIcon(os.path.join(SYS_IMG_FOLDER,
                                                               'preferences-system.png')), '&Preferences', self)
        preferenceWin.setShortcut('Ctrl+P')
        preferenceWin.setStatusTip("Application Preferences")
        #preferenceWin.triggered.connect()
        
        # Toolbar
        self.toolbar = self.addToolBar('File')
        self.toolbar.addAction(newProject)
        self.toolbar.addAction(exitAction)
        self.toolbar_project = self.addToolBar('Project')
        self.toolbar_project.addAction(preferenceWin)
        
        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newProject)
        fileMenu.addAction(exitAction)
        prefMenu = menubar.addMenu('&Project')
        helpMenu = menubar.addMenu('&Help')
        
        prefMenu.addAction(preferenceWin)
        
        
        
        #fileMenu.addAction(exitAction)
                
    def status(self, message):
        self.statusBar().showMessage(message)