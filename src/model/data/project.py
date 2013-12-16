'''
Model that contains an array of components that make up the Project
'''
class ProjectData:
    
    ''' Q Standard Item '''
    qsi_proj = None
    save = False
    
    def __init__(self, qsi):
        self.qsi_proj = qsi
        self.save = True # When created, it needs to be saved
    