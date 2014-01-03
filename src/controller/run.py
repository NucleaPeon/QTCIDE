from PyQt4 import QtGui, QtCore

import os
import model.run
import view.actions.project.build.build as build
import view.modal.QtPopupTextInput
'''
Run controller

:Description:
    Contains methods for managing, configuring and
    communicating with interpreters, compilers and
    other binary/project invocations on the operating system
'''

def add_run_config(name, icon=None):
    qtstd = QtGui.QStandardItem(name)
    if not icon is None:
        qtstd.setIcon(icon)
    else:
        qtstd.setIcon(build.BuildSystemBuildAction().qicon)
    qtstd.appendRow(QtGui.QStandardItem(
        model.run.Run().qicon,
        "Default Run"))
    model.run.Run().runs.appendRow(qtstd)
    
def remove_run_config(*args):
    print("remove_run_config")