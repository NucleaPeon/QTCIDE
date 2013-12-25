'''
Compiler controller

:Description:
    Contains methods for managing, configuring and
    communicating with compilers on the operating system
'''

import os
import model.run

#def saveProject(project_model, dir_path=None, ext="qtc"):
    #'''
    
    #:Throws:
        #- SaveException: Attempt to save did not succeed, therefore
          #stop function so user can understand the issue and potentially
          #fix it.
    #'''
    #if dir_path is None:
        #dir_path = ''
    #path = os.path.join(os.environ['HOME'],
                        #dir_path,
                        #"{}.{}".format(project_model.text(), ext))
    #proj = model.project.Project()
    #f = open(path, 'w')
    #f.write("Hello World")
    #f.close()
    