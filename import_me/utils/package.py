class MyImportException(Exception):
    """A placeholder exception."""

def import_me():
    raise MyImportException("You have been successful to import me.")
