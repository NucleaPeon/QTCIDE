from PyQt4 import QtGui, QtCore
from view.img import SYS_IMG_FOLDER, SYS_APP_ICON
import view.actions.project.build.build as build
import view.menu.runcontext
import view.modal.QtPopupConfirm
import view.modal.QtPopupTextInput
import controller.run
import os


'''
Run consists of a series of parameters that define how the
program is used. 

For languages such as C/C++, this involves selecting a compiler
and a main method(). For java, the JVM must be defined. For Python,
the python interpreter and either the module or module.method is
defined. 

QTCIDE's Run configurations are highly extensible. Most people who 
understand IDE's should be familiar with eclipse's Run configurations, 
as that is what this is somewhat based off of. 

:Some background information:
    A Run object is based off a Build object.
    A Build object defines what groups of files are included
    into binaries, packages or other organized structures, as
    well as the entry point when the final product is run.
    
    A Run object defines a particular aspect on how the user
    would manipulate or utilize the finished product.
    For instance, once a build defines the binaries and where
    the binaries get installed on the Operating System (example:
    Makefile), a run file can be produced to act on the installed
    binary.
    
What can a Run configuration do?

It can: 
    - Run a test suite on the finished product (defining a test suite
      and running it doesn't require an explicit run configuration;
      right-clicking a test suite has a default run and will build
      the project before running by default)
    - It can run external programs before, during and after the
      binary is run
    - It can call methods other than main(), allowing for pre-setup
      without a test suite. It can completely bypass main(), or ignore
      the binary completely (Run programs that in turn would run the
      main binary, aka invoking dependant programs. One use case for
      this is to launch a webpage that may have a cgi script written
      in python or c that gets run on page launch)
    
'''
class Run:
    
    _instance = None # Single instance of initialized class
    
    def __new__(self,  *args, **kwargs):
        if not self._instance:
            self._instance = super(Run, self).__new__(
                self, *args, **kwargs)
            self.runs = QtGui.QStandardItemModel() # Project data
            self.runs.setHorizontalHeaderItem(0, 
                                                  QtGui.QStandardItem("Configurations"))
            self.rootNode = self.runs.invisibleRootItem()
            self.qicon = QtGui.QIcon(os.path.join(SYS_IMG_FOLDER, 'configure.png'))
            test = QtGui.QStandardItem(build.BuildSystemBuildAction().qicon, "gcc")
            test.setEditable(False)
            test.appendRow(QtGui.QStandardItem(self.qicon, "Test Build Configuration"))
            self.rootNode.appendRow(test)
            self.runtree = QtGui.QTreeView()
            self.runcontextmenu = view.menu.runcontext.RunContextMenu()
            self.runtree.setModel(self.runs)
        return self._instance
    
    def configure_run(self):
        print("model.run.Run")
        
    def add_run_config(self):
        view.modal.QtPopupTextInput.QTextInputPopup("Add New Run Type", "Run Type",
                             success=lambda: controller.run.add_run_config("test"))
    
    def remove_run_config(self):
        view.modal.QtPopupConfirm.getTextPopup(None, "Remove Run Configuration", "Confirm Removal?",
                             success=controller.run.remove_run_config, 
                             failure=print)
        index = self.runtree.currentIndex()
        print("{}, {}".format(index.row(), index.column()))