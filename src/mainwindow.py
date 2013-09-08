#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base.window import Window
from PyQt4 import QtGui, QtCore
from base.settings import Settings as s

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle(QtGui.QApplication.translate("C and C++ Development Environment", 
                                                         "C and C++ Development Environment", 
                                                         None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.hide()
        self.setCentralWidget(self.centralwidget) 
        
        #self.setWindowIcon(QtGui.QIcon('src/web.png'))
        # X, Y, Width, Height
        #if s.custom_dimensions:
            #if s.fullscreen:
                #screen = QtGui.QDesktopWidget().screenGeometry()
                #self.setGeometry(0, 0, screen.width(), screen.height())
            #else:
                #self.setGeometry(s.x, s.y, s.width, s.height)
        
        
        self.dock1Widget = QtGui.QDockWidget(self)
        self.dock1Widget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dock1Widget.setWindowTitle(QtGui.QApplication.translate("self", "dock1", None, QtGui.QApplication.UnicodeUTF8))
        self.dock1WidgetContents = QtGui.QWidget()
        self.dock1Widget.setWidget(self.dock1WidgetContents)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock1Widget)
        
        # Set Statusbar message (included in MainWindow)
        self.status("Ready")
        
        # Actions
        
        exitAction = QtGui.QAction(QtGui.QIcon('img/system-shutdown.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        newProject = QtGui.QAction(QtGui.QIcon('img/document-new.png'), '&New Project', self)
        newProject.setShortcut('Ctrl+N')
        newProject.setStatusTip('New Project')
        
        preferenceWin = QtGui.QAction(QtGui.QIcon('img/preferences-system.png'), '&Preferences', self)
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