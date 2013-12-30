'''
model/state is a folder where state machines are kept: modules that connect 
various ui components and their state to actions and controller methods. 

A State Machine is a collection of arrays that contain callable methods
upon invocation. 

a SaveProject state machine will go through the action's setEnabled method
as well as all the persistance methods of every changed source code file.

That way all paths of each action (which can also call other state machines)
are laid out in a simple, easy to read manner and can be changed from one 
place. 

More research should be done on the optimal way to keep track of signals
and slots in pyqt4. 
'''

