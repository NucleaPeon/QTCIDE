'''
Project Setting Window Configuration

:Description:
    Due to the dynamic nature of this program, adding links to Classes
    that inherit view.modal.config.ProjectSettingsPane.ProjectSettingsPane()
    (but do not instantiate them) in a dictionary of {"name": class reference}
    key/value pairs allows us to dynamically add setting capabilites.
    
    For instance, if we wanted to add another new fancy build system,
    adding a settings window for that with default settings is easy.
    - Create the view.modal.config.ProjectSettingsPane.ProjectSettingsPane
      class, place it in a module found in view/modal/config/settings/ folder
      and add its name/class reference here in this file, and it should
      automatically appear if done right.
      
    - The settings window may have to import modules from view/model/controller
      folder roots to change modified attributes.
'''

import view.modal.config.settings.build
import view.modal.config.settings.project
import view.modal.config.settings.plugins

qidesettings = {'Project': view.modal.config.settings.project.Project,
                'Build': view.modal.config.settings.build.Build,
                'Plugins': view.modal.config.settings.plugins.Plugins}