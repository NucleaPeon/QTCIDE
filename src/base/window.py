#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

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
        self.setGeometry(200, 200, 800, 500)
