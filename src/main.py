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
import argparse
import cache
import view.window 

def pyqt4_is_installed():
    
    try:
        from PyQt4 import QtGui
    except Exception as E:
        sys.stderr.write("PyQT4 is not installed or could not be found")
        sys.stderr.write(str(E))
        return False
    return True

def main():
    '''
    '''
    # Add to path
    # Until software can be properly installed onto the OS and paths become
    # predictable, assume running from top level directory
    sys.path.append(os.path.join(os.getcwd(),
                              os.path.dirname(__file__)))

    ### Launch UI ###
    from PyQt4 import QtGui
    #from view.mainwindow import MainWindow
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(shutdown) 
    #mw = mainwindow.MainWindow()
    #mw.show()
    cache.cache()
    win = view.window.Window()
    win.show()
    
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    sys.exit(app.exec_())
    
def shutdown():
    print("Shutdown")


###
### Start parsing arguments from the command line here:
###
if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser(description='QT-Based Drag and Drop IDE')
    args = parser.parse_args(sys.argv[1:])
    
    main()
