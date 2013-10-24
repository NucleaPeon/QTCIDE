'''
Menu Configuration File

:Description:
    Contains all information regarding menu bars, menus and menu items with
    associated settings. This is parsed and initialized then added to 
    MainWindow.
    

'''



'''
:Description:
    Format:
    
        {
          key: integer - Position from Left to Right appearing in the menu bar
          value: dict - Menu
          {
            key: string - Name of Menu
            value: dict - list of sub-menu items
            [
              item - dict - menu item attribute found in class
              {
                key: attributes
                    - icon: string (or None) for icon path and name
                    - name: string name of MenuItem
                    - callback: callable attribute
                    - visible: boolean default visibility
                    - sub : dict submenu definition, same as "item - dict" format
                value: attribute assignment (see above)
              }
            ]
          }      
        }
'''
MENUS = {0: {'File': [{'new_project': {'icon': None,
                                       'name': 'New Project',
                                       'callback': print,
                                       'visible': True,
                                       'sub': None }}, 
                      'close_project': {'name': 'Close Project'}, 
                      'quit': {'name': 'Exit Application'}]},
         1: {'View': ['Docks']},
         2: {'Project': ['Preferences']},
         3: {'Help' : ['About']}}