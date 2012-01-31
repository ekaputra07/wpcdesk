#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from mainWindow import Ui_mainWindow
import xmlrpclib

class wpcDesk(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.actionRefresh, QtCore.SIGNAL("activated()"), self.showConnectionSettings)

    def showConnectionSettings(self):
        server_url = 'http://balitechy.com/xmlrpc.php'
        server = xmlrpclib.Server(server_url)
        extra = {'number':20}
        comments = server.wp.getComments(1, 'admin', 'veraka1985', extra)

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



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wpcdesk = wpcDesk()
    wpcdesk.show()
    sys.exit(app.exec_())

