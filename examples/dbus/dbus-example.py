import sys
import os
import dbus
import dbus.service
from dbus.mainloop.qt import DBusQtMainLoop
from PyQt4 import QtGui

INTERFACE = 'org.qtcide'

class DbusTest(dbus.service.Object):

    def __init__(self):
        busName = dbus.service.BusName(INTERFACE, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/org/qtcide/test/dbus')
        

    @dbus.service.method(INTERFACE,
                        in_signature = 's', out_signature = 's')
    def NewProject(self, name):
        return name
    
if __name__ == "__main__":
    
    DBusQtMainLoop(set_as_default = True)    
    
    app = QtGui.QApplication(sys.argv)
    ref = DbusTest()

    sys.exit(app.exec_())
    
