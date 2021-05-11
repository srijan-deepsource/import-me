"""This is not a test file. I am just trying to import `import_me` and run it."""
from import_me.utils.package import import_me, MyImportException

try:
    import_me()
except MyImportException as exc:
    print("Voila!")
    print(exc)
