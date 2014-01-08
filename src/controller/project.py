'''

'''

import os
import model.project

def saveProject(name, dir_path=None, ext="qtc"):
    '''
    :Description:
        Saves the project by gathering project data and persisting it
        in xml format to a file on the underlying (or cloud) filesystem.
    
    :Throws:
        - SaveException: Attempt to save did not succeed, therefore
          stop function so user can understand the issue and potentially
          fix it.
    '''
    if dir_path is None:
        dir_path = ''
    path = os.path.join(os.environ['HOME'],
                        dir_path,
                        "{}.{}".format(project_model.text(), ext))
    proj = model.project.Project()
    f = open(path, 'w')
    f.write("Hello World")
    f.close()
    
def persist(fsys, proj_data):
    print("TODO: Filesystem location persistance: local/cloud/remote")