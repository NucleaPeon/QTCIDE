'''
:Description:
    This class represents a Qt Window that requests a Question
    with a label.
    
    Example: When removing a configuration file, prompt user and
             only perform removal on OK button
             
'''
import sys
from PyQt4 import QtGui, QtCore

def getTextPopup(parent=None, title='Test', question="Are you sure?", success=None,
                 failure=None):
    '''
    :Description:
        A popup that requests the user input text. Has an OK and Cancel
        button, when OK is clicked, input text is sent to the callback
        as the first parameter.
        
    :Parameters:
        - parent; QWidget: Because this method isn't in a class that is
          a widget, it requires a Widget to display itself (in a qt exec loop)
          so the calling QWidget should put "self" for that attribute.
        - title; string: Title of popup window
        - question; string: What to ask the user
        - callback; callable object, method: On OK, send result to this 
          method
    '''
    qdialog = QtGui.QDialog(parent)
    dialog_layout = QtGui.QVBoxLayout()
    button_layout = QtGui.QHBoxLayout()
    dialog_layout.addWidget(QtGui.QLabel(question))
    
    
    buttonBox = QtGui.QDialogButtonBox(qdialog)
    buttonBox.setOrientation(QtCore.Qt.Horizontal)
    buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
    buttonBox.accepted.connect(qdialog.accept)
    buttonBox.rejected.connect(qdialog.reject)
    if not success is None:
        buttonBox.accepted.connect(success)
    if not failure is None:
        buttonBox.rejected.connect(failure)
    
    dialog_layout.addWidget(buttonBox)
    qdialog.setLayout(dialog_layout)
    qdialog.setWindowTitle(title)
    
    qdialog.exec_()
    #
    #if ol:
    #    return callback(text)
    #return None