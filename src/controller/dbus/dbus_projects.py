import dbus
import dbus.service
from controller.dbus import INTERFACE
import model.project
import yaml

'''
:Dependencies:

'''


class Dbus(dbus.service.Object):

    def __init__(self):
        busName = dbus.service.BusName(INTERFACE, bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/org/qtcide')

    @dbus.service.method('qtcide.Projects',
                        in_signature = 's', out_signature = 's')
    def NewProject(self, name):
        proj = model.project.createNewProject(name)
        
        return proj.name
    
    @dbus.service.method('qtcide.Projects',
                        in_signature = '', out_signature = '')
    def InitTestProjectData(self):
        return mwin.MainWindow().initTestData()