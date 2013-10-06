import dbus
import dbus.service
from src.dbus import INTERFACE
import src.mainwindow as mwin

class Dbus(dbus.service.Object):

    def __init__(self):
        busName = dbus.service.BusName(INTERFACE, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/org/qtcide')

    @dbus.service.method('qtcide.Projects',
                        in_signature = 's', out_signature = 's')
    def NewProject(self, name):
        return mwin.MainWindow().addNewProject(name)