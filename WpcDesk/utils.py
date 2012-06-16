# This is to check if QString is available from QtCore and import it.
# otherwise return QString as a normal python String. (latest version of PyQt4)

try:
    from QtCore import QString
except ImportError:
    QString  = str


def str_to_qstr(string):
    """Shortcut to convert QString to Python String"""
    return QString(string)
