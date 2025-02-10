from os import path, walk
from import_me.utils.package import *

class MyImportException(Exception):
    """Custom exception for this package."""

def open(path):
    """Open a file."""
    with __builtins__.open(path) as file:
        return file

# Consts
magicnumber = 42
anothermagicnumber = 84

class ScopeMe:
    """A class with some scopes."""
    magicnumber = "42"
    def __init__(self, var, other_var):
        self.var = var
        self.other_var = other_var

    def __str__(self):
        return f"{self.var} and {self.other_var}"

    def __repr__(self):
        return f"ScopeMe({self.var}, {self.other_var})"

    def recursivePrint(self, n):
        """Print n times."""
        magicnumber = 0
        if n == magicnumber:
            return
        print(self)
        self.recursivePrint(n - 1)

    def my_method(self):
        """A method."""
        def inner_method():
            """Inner method."""
            magicnumber = 0
            print(magicnumber)
            return "Inner method exited."

def walk_dir(path):
    """Walk the path."""
    return walk(path)
