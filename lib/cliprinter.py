#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:Description:
    Manages printing on the command line in a *consistent* way,
    providing tabs when applicable and dynamic lists, etc.
"""

def indent_by(num):
    """
    :Description:
        Returns a string with the correct number of indentations
        
    :Returns:
        - string: indentation string
    """
    indent = ""
    for i in range(0, num):
        indent += "\t"
    return indent

def prnt(string, indent=0, prefix="", suffix=""):
    """
    :Description: 
        Prints a line with contents specified in header
        
    :Returns:
        - string: fully formed string with parameters embedded in it properly
    """
    line = "%s%s%s%s" % (indent_by(indent), prefix, string, suffix)
    print(line)
    return line
