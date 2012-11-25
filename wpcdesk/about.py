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


from PyQt4 import QtGui
from gui.about_window import Ui_AboutWindow

class AboutWindow(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

