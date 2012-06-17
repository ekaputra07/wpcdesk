#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import sys
from PyQt4 import QtGui
from main import wpcDesk


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wpcdesk = wpcDesk()
    wpcdesk.showMaximized()
    sys.exit(app.exec_())

