import model.project

class Project:
    
    @staticmethod
    def addNewProject(proj_name):
        model.project.Project().addNewProject(proj_name)