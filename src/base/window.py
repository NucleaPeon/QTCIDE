#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, Qt
import widgets.pane as pane

class Window(QtGui.QWidget):
    '''
    :Description:
        This is the class that sits in the MainWindow object
    '''
    
    def __init__(self, **kwargs):
        super(Window, self).__init__()
        layout = QtGui.QGridLayout()
        layout.addWidget(pane.Pane(**kwargs), 0, 0)
        self.setLayout(layout)
