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


import sys, os
import pickle
import bz2

from PyQt4 import QtGui, QtCore
from gui.settings_window import Ui_formConfig

__configpath__ = os.path.expanduser('~/.wpcdesk')

def get_connection_settings():
    """Get connection setting from config file."""
    data = {}
    try:
        cfile = open(__configpath__, 'rb')
        data = pickle.load(cfile)
        cfile.close()
    except:
        QtGui.QMessageBox.warning(self, 'Warning!','Failed to read cofiguration file,\nMake sure "%s" file is readable.' % __filename__, QtGui.QMessageBox.Ok)
    return data


class ConnectionSettings(QtGui.QDialog):
    """Main class for Connection Setting Window"""

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_formConfig()
        self.ui.setupUi(self)

        self.pull_data()

        QtCore.QObject.connect(self.ui.btnSave, QtCore.SIGNAL("clicked()"), self.saveConfig)

    def pull_data(self):
        if self.is_config_exists:
            data = self.read_from_file()
            self.ui.serverEdit.setText(data.get('server',''))
            self.ui.usernameEdit.setText(data.get('username',''))
            self.ui.passEdit.setText(data.get('password',''))

            self.ui.nameEdit.setText(data.get('name',''))
            self.ui.emailEdit.setText(data.get('email',''))
            self.ui.UrlEdit.setText(data.get('url',''))
        return


    @property
    def is_config_exists(self):
        if os.path.isfile(__configpath__):
            return True
        return False

    def save_to_file(self, data):
        try:
            cfile = open(__configpath__, 'wb')
            pickle.dump(data, cfile, 1)
            cfile.close()
            QtGui.QMessageBox.information(self, 'Information','Settings saved.', QtGui.QMessageBox.Ok)
        except:
            QtGui.QMessageBox.warning(self, 'Warning!','Failed to write cofiguration file,\nMake sure "%s" file is writable.' % __filename__, QtGui.QMessageBox.Ok)

    def read_from_file(self):
        data = {}
        data = get_connection_settings()
        return data

    def saveConfig(self):
        server = self.ui.serverEdit.text()
        username = self.ui.usernameEdit.text()
        password = self.ui.passEdit.text()
        name = self.ui.nameEdit.text()
        email = self.ui.emailEdit.text()
        url = self.ui.UrlEdit.text()

        if not server:
            QtGui.QMessageBox.warning(self, 'Warning!','Please provides your WordPress XML-RPC Server URL.\nUsually http://yourdomain.com/xmlrpc.php', QtGui.QMessageBox.Ok)
            return False

        if not username:
            QtGui.QMessageBox.warning(self, 'Warning!','Please provides your WordPress login username.', QtGui.QMessageBox.Ok)
            return False

        if not password:
            QtGui.QMessageBox.warning(self, 'Warning!','Please provides your WordPress login password.', QtGui.QMessageBox.Ok)
            return False

        data = {
            'server': server,
            'username': username,
            'password' : password,
            'name': name,
            'email': email,
            'url': url,
            }

        self.save_to_file(data)

        return True

