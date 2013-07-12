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
    