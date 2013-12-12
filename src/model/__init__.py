import importlib

def model(modname):
    '''
    :Description:
        model returns the model object of the current controller
        __name__ variable
        
    :Parameter:
        - modname: the module path found in the __name__ variable
        
    :Returns:
        Class object
        
        It is found by converting the last string after
        splitting the module path by "." character into titlecase.
        Example: if __name__ equals "controller.module", this method
        parses the content into ["controller", "module"] and imports
        "model.module" and returns model.module.Module.
        
    :Requirements:
        In order to import the model properly, it must be a titlecase
        version of the module filename. Otherwise, a None will be returned.
        
        A Model cannot have a constructor with parameters, or at a minimum,
        required named parameters. (*args and **kwargs are acceptable)
        
    :See:
        - model.__init__.py
    '''
    lstname = modname.split(".")
    name = lstname[len(lstname)-1]
    mod = importlib.import_module("model.{}".format(name))
    try:
        cls = getattr(mod, name.title())
        return cls
    except:
        return None
    
    