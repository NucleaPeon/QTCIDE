#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from settings import Settings as s

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.initialize()
        
    def initialize(self):
        
        #edit = QtGui.QLineEdit('', self)
        #edit.setDragEnabled(True)
        #edit.move(30, 65)
        
        #button = Button("Button", self)
        #button.move(190, 65)
        
        self.setWindowTitle('C / C++ Integrated Development Environment')
        # X, Y, Width, Height
        if s.custom_dimensions:
            if s.fullscreen:
                screen = QtGui.QDesktopWidget().screenGeometry()
                self.setGeometry(0, 0, screen.width(), screen.height())
            else:
                self.setGeometry(s.x, s.y, s.width, s.height)
