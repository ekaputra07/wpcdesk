# -*- coding: utf-8 -*-

import sys, os
import pickle
import bz2

from PyQt4 import QtGui, QtCore
from settingsWindow import Ui_formConfig

__filename__ = 'config.cfg'
__configpath__ = os.path.join(os.path.abspath(os.path.dirname(__file__)), __filename__)

class SettingsWindow(QtGui.QDialog):
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
        return


    @property
    def is_config_exists(self):
        if os.path.isfile(__configpath__):
            return True
        return False

    def save_to_file(self, data):
        try:
            cfile = open(__configpath__, 'wb')
            pickle.dump(data, cfile)
            cfile.close()
            QtGui.QMessageBox.information(self, 'Information','Settings saved.', QtGui.QMessageBox.Ok)
        except:
            QtGui.QMessageBox.warning(self, 'Warning!','Failed to write cofiguration file,\nMake sure "%s" file is writable.' % __filename__, QtGui.QMessageBox.Ok)

    def read_from_file(self):
        data = {}
        try:
            cfile = open(__configpath__, 'rb')
            data = pickle.load(cfile)
            cfile.close()
        except:
            QtGui.QMessageBox.warning(self, 'Warning!','Failed to read cofiguration file,\nMake sure "%s" file is readable.' % __filename__, QtGui.QMessageBox.Ok)
        return data

    def saveConfig(self):
        server = self.ui.serverEdit.text()
        username = self.ui.usernameEdit.text()
        password = self.ui.passEdit.text()

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
            'password' : password
            }

        self.save_to_file(data)

        return True

