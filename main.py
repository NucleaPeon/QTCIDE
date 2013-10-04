#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:Author:
    - Daniel Kettle
    
:Copyright:
    - (C) 2013 Daniel Kettle, Peon Developments Inc.
    - (C) 2013 Southern Alberta Institute of Technology
    
:Date:
    - June 14 2013

:Description:
    Main Application launch script.
    
    CLI Argument Parsing is done from the /bin/ folder, which in turn imports
    and calls the main method.
"""
import os
import sys
import lib.cliprinter as clip
import argparse
import importlib
import dbus
import dbus.service
from dbus.mainloop.qt import DBusQtMainLoop

# GLOBAL DBUS INTERFACE FOR QTCIDE
INTERFACE = 'org.qtcide'


class Dbuss(dbus.service.Object):
    
        
    def __init__(self):
        busName = dbus.service.BusName(INTERFACE, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/org/qtcide')

    @dbus.service.method(INTERFACE,
                        in_signature = '', out_signature = 's')
    def HelloWorld(self):
        return "Hello World"

def pyqt4_is_installed():
    
    try:
        from PyQt4 import QtGui
    except Exception as E:
        sys.stderr.write("PyQT4 is not installed or could not be found")
        sys.stderr.write(str(E))
        return False
    return True

def load_all_dbus_modules():
    '''
    :Description:
        Imports dbus methods into QTCIDE found in the src/dbus/ directory
        
        NOTE: Certain module names like "test.py" will fail because there
        may be a test/ directory on the operating system.
        Ex: /usr/lib64/python3.2/test/ on my system contains many python
            files for testing (unittest)
        
    :Returns:
        - tuple: dbus python modules
    '''
    mods = []
    from src.dbus import SYS_DBUS_FOLDER
    sys.path.append(SYS_DBUS_FOLDER)
    for _file in os.listdir(SYS_DBUS_FOLDER):
        if _file.endswith(".py") and not _file.startswith("_"):
            mod = importlib.import_module(_file.rstrip('.py'))
            if hasattr(mod, 'Dbus'):
                print("Module has Dbus object")
                mods.append(mod.Dbus())
    return tuple(mods)

def main():
    '''
    '''
    clip.prnt("Initializing C/C++ IDE")
    clip.prnt("[Checking if PyQT4 is installed] \t: {}".format(pyqt4_is_installed()),
         indent=1, prefix="DEP - ")
    # Add to path
    # Until software can be properly installed onto the OS and paths become
    # predictable, assume running from top level directory
    sys.path.append(os.path.join(os.getcwd(), 'base'))

    ### Launch UI ###
    from PyQt4 import QtGui
    from src.mainwindow import MainWindow
    #pid = os.fork()
    DBusQtMainLoop(set_as_default = True)
    #if pid > 0:
        ## Exit first parent.
        #sys.exit(0)
    
    app = QtGui.QApplication(sys.argv)
    # Add Dbus Services after QApplication initialization
    a = load_all_dbus_modules()
    app.aboutToQuit.connect(shutdown) 
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
    

    
def shutdown():
    print("Shutdown")


###
### Start parsing arguments from the command line here:
###
if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser(description='QT-Based C/C++ Development IDE')
    args = parser.parse_args(sys.argv[1:])
    
    main()
