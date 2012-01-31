#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from mainWindow import Ui_mainWindow
from settings import SettingsWindow

import xmlrpclib


class wpcDesk(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.settings = SettingsWindow()

        QtCore.QObject.connect(self.ui.actionRefresh, QtCore.SIGNAL("activated()"), self.loadComments)
        QtCore.QObject.connect(self.ui.actionConnection, QtCore.SIGNAL("activated()"), self.showConfigWindow)

    def loadComments(self):
        if not self.settings.is_config_exists:
            QtGui.QMessageBox.warning(self, 'Warning!','Connection settings not available.', QtGui.QMessageBox.Ok)
            self.settings.exec_()
        else:
            data = self.settings.read_from_file()
            server_url = str(data.get('server', ''))
            username = str(data.get('username', ''))
            password = str(data.get('password', ''))

            server = xmlrpclib.Server(server_url)
            extra = {'number':20}
            comments = []
            try:
                comments = server.wp.getComments(1, username, password, extra)
            except:
                QtGui.QMessageBox.warning(self, 'Warning!','Failed connecting to server,\nMake sure connection setting is correct.', QtGui.QMessageBox.Ok)

            if comments:
                self.ui.tblComments.setRowCount(len(comments))
                row = 0
                for comment in comments:
                    self.ui.tblComments.setItem(row, 0, QtGui.QTableWidgetItem(QtCore.QString(comment['comment_id'])))
                    self.ui.tblComments.setItem(row, 1, QtGui.QTableWidgetItem(''))
                    self.ui.tblComments.setItem(row, 2, QtGui.QTableWidgetItem(comment['status']))
                    self.ui.tblComments.setItem(row, 3, QtGui.QTableWidgetItem(comment['author']))
                    self.ui.tblComments.setItem(row, 4, QtGui.QTableWidgetItem(QtCore.QString(comment['content'][:50])))
                    self.ui.tblComments.setItem(row, 5, QtGui.QTableWidgetItem(comment['post_title']))
                    row += 1

                self.ui.tblComments.resizeColumnsToContents()

    def showConfigWindow(self):
        self.settings.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wpcdesk = wpcDesk()
    wpcdesk.show()
    sys.exit(app.exec_())

