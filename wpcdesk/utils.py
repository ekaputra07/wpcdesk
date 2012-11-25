#  wpcdesk - WordPress Comment Desktop
#  Copyright (C) 2012 Eka Putra - ekaputra@balitechy.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


# This is to check if QString is available from QtCore and import it.
# otherwise return QString as a normal python String. (latest version of PyQt4)

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString  = str


def str_to_qstr(string):
    """Shortcut to convert QString to Python String"""
    return QString(string)
