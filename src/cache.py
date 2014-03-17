'''
Contains instantiated objects that can be shared from all
portions of the user interface to remove the need for
singleton patterns.
'''
import os
import importlib

# Step through this folder
CACHE_DIR = os.path.join(os.getcwd(),
                         os.path.dirname(__file__), 'view')
'''
Cache instantiated classes here
NOTE: In order to cache a class into the CACHE dict, the module must contain
a CACHE array of module strings to point to the classes they want preloaded.
The module string becomes part of the key:

    module "view.component.example" with classes "Example1",
    "Example2" and "Example1.Example3".
    
    Class Strings are placed into CACHE = [...]
    
    Upon caching, the variable is read and an instance of each class loaded
    into {'view.component.example.Example1': <class 'Example1' memaddr0x100344...>}
    etc.
    
'''
CACHE = {}

def load(key):
    return CACHE.get(key, None)
#FIXME: None should be new object if not cached

def cache(start = CACHE_DIR, key = 'view'):
    '''
    Cache all modules in a dynamic dictionary that associates
    path strings with the loaded object for use in any portion
    of the view so singletons can be removed.
    
    Only load .py modules, ignore anything with a prefixed "_"
    
    :Parameters:
        - start: Path to start searching modules from
        - path_prefix: This is what becomes the dictionary key
    '''
    def search(path, key):
        for f in os.listdir(path):
            if f[0] == "." or f[0] == "_":
                continue
            module = os.path.join(path, f)
            if os.path.isdir(module):
                search(module, key + "." + f)
            else:
                root, ext = os.path.splitext(f)
                if ext == ".py":
                    m = importlib.import_module(key + "." + root)
                    if hasattr(m, "CACHE"):
                        for x in m.CACHE:
                            cls = getattr(m, x)
                            CACHE["{}.{}.{}".format(key, root, x)] = cls()
            
    
    search(start, key)
    print(CACHE)