#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base.window import Window
from PyQt4 import QtGui, QtCore
from base.settings import Settings as s

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setCentralWidget(Window())
        self.setWindowTitle('C / C++ Integrated Development Environment')
        #self.setWindowIcon(QtGui.QIcon('src/web.png'))
        # X, Y, Width, Height
        if s.custom_dimensions:
            if s.fullscreen:
                screen = QtGui.QDesktopWidget().screenGeometry()
                self.setGeometry(0, 0, screen.width(), screen.height())
            else:
                self.setGeometry(s.x, s.y, s.width, s.height)
                
        # Set Statusbar message (included in MainWindow)
        self.status("Ready")
        
        # Actions
        exitAction = QtGui.QAction(QtGui.QIcon('img/system-shutdown.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        # Toolbar
        self.toolbar = self.addToolBar('File')
        self.toolbar.addAction(exitAction)
        
        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        helpMenu = menubar.addMenu('&Help')
        
        
        
        #fileMenu.addAction(exitAction)
                
    def status(self, message):
        self.statusBar().showMessage(message)