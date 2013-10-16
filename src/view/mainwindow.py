#!/usr/bin/env python3
import os
import view.base.window as window
from PyQt4 import QtGui, QtCore
import view.docks.project as project
import controller.settings as s
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON


class MainWindow(QtGui.QMainWindow):
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(MainWindow, self).__new__(
                self, *args, **kwargs)
        return self._instance
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.settings = s.Settings()
        self.resize(self.settings.width, self.settings.height)
        self.setWindowTitle(QtGui.QApplication.translate("C and C++ Development Environment", 
                                                         "C and C++ Development Environment", 
                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = window.Window()
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
        self.dockProjectContents = project.ProjectDock()
        self.dockProject.setWidget(self.dockProjectContents)
        
        self.dockBuild = QtGui.QDockWidget(self)
        self.dockBuild.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockBuild.setWindowTitle(QtGui.QApplication.translate(
            "self", "Build Options", None, QtGui.QApplication.UnicodeUTF8))
        self.dockBuildContents = QtGui.QWidget() #FIXME: This can go into its own module?
        self.dockBuild.setWidget(self.dockBuildContents)
        
        self.dockCompiler = QtGui.QDockWidget(self)
        self.dockCompiler.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockCompiler.setWindowTitle(QtGui.QApplication.translate(
            "self", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.dockCompilerContents = QtGui.QWidget() #FIXME: This can go into its own module?
        self.dockCompiler.setWidget(self.dockCompilerContents)
        
        self.dockTest = QtGui.QDockWidget(self)
        self.dockTest.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockTest.setWindowTitle(QtGui.QApplication.translate(
            "self", "Testing Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.dockTestContents = QtGui.QWidget() #FIXME: This can go into its own module?
        self.dockTest.setWidget(self.dockTestContents)
        
        #self.dock = QtGui.QDockWidget(self)
        #self.dock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        #self.dock.setWindowTitle(QtGui.QApplication.translate(
            #"self", "", None, QtGui.QApplication.UnicodeUTF8))
        #self.dockContents = QtGui.QWidget() #FIXME: This can go into its own module?
        #self.dock.setWidget(self.dockContents)
        
        
        '''
        Qt::LeftDockWidgetArea  0x1
        Qt::RightDockWidgetArea 0x2
        Qt::TopDockWidgetArea   0x4
        Qt::BottomDockWidgetArea        0x8
        Qt::AllDockWidgetAreas  DockWidgetArea_Mask
        Qt::NoDockWidgetArea    0
        '''
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockProject)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockBuild)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockCompiler)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockTest)
        
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
        
        helpAbout = QtGui.QAction('&About', self)
        helpAbout.setShortcut('Ctrl+A')
        helpAbout.setStatusTip("About the Program")
        
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
        viewMenu = menubar.addMenu('&View')
        viewMenu.addMenu('&Docks')
        #viewMenu.addAction()
        prefMenu = menubar.addMenu('&Project')
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(helpAbout)
        
        prefMenu.addAction(preferenceWin)
        #fileMenu.addAction(exitAction)
    
    def addNewProject(self, name):
        return self.dockProjectContents.newProject(name)
    
    def initTestData(self):
        pass
            
    def status(self, message):
        self.statusBar().showMessage(message)
        
    