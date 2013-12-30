'''
model/state is a folder where state machines are kept: modules that connect 
various ui components and their state to actions and controller methods. 

A State Machine is a collection of arrays that contain callable methods
for each action.
(pseudocode, not exact syntax)
SaveProject action would have [sourcecode.save() for sourcecode in all_source_code_files,
                               saveaction.setEnabled(False)]

Constructors for actions should connect their triggered callback to a method that
calls all these methods.
'''

