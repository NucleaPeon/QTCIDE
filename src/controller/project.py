'''

'''

import os

def saveProject(project, dir_path=None, ext="qtc"):
    if dir_path is None:
        dir_path = ''
    path = os.path.join(os.environ['HOME'],
                        dir_path,
                        "{}.{}".format(project, ext))
    
    print(path)
    #f = open()
    #f.write("Hello World")
    #f.close()
    