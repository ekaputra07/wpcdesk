# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from gui.main_window import Ui_mainWindow
from settings import ConnectionSettings
from about import AboutWindow
from wpcdesk_threads import GetCommentsThread
import time

import xmlrpclib


def str_to_qstr(string):
    """Shortcut to convert QString to Python String"""
    return QtCore.QString(string)

class wpcDesk(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.settings = ConnectionSettings()

        QtCore.QObject.connect(self.ui.actionRefresh, QtCore.SIGNAL("activated()"), self.loadComments)
        QtCore.QObject.connect(self.ui.actionConnection, QtCore.SIGNAL("activated()"), self.showConfigWindow)
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("activated()"), self.showAboutWindow)

        self.get_comments_thread = GetCommentsThread()
        self.get_comments_thread.response_received.connect(self.display_comments)
        self.get_comments_thread.error_raised.connect(self.display_errmsg)
        self.get_comments_thread.is_loading.connect(self.update_progressbar)
        self.get_comments_thread.status_updated.connect(self.update_status)

        if not self.settings.is_config_exists:
            self.update_status('Connection settings not available.')
        else:
            self.update_status('Ready to connect.')

        self.ui.progressBar.hide()
        #self.loadComments()


    def loadComments(self):
        if not self.settings.is_config_exists:
            QtGui.QMessageBox.warning(self, 'Warning!','Connection settings not available.', QtGui.QMessageBox.Ok)
            self.settings.exec_()
        else:
            self.get_comments_thread.start()

    def display_comments(self, comments):
        if comments:
            self.ui.tblComments.setRowCount(len(comments))
            row = 0
            for comment in comments:
                #list key should be called with QtCore.QString('key_name') because returned value from Thread
                #is a list of QString objects
                #a str_to_qstr function used for shortcut
                self.ui.tblComments.setItem(row, 0, QtGui.QTableWidgetItem(comment[str_to_qstr('comment_id')]))

                #should be converted to standard datetime format
                #because datetime returned by xmlrpclib is a datetime instance
                #http://docs.python.org/library/xmlrpclib.html#module-xmlrpclib
                date_instance = comment[str_to_qstr('date_created_gmt')]
                time_tpl = date_instance.timetuple()
                date = time.strftime("%b %d, %Y %H:%M", time_tpl)


                self.ui.tblComments.setItem(row, 1, QtGui.QTableWidgetItem(date))
                self.ui.tblComments.setItem(row, 2, QtGui.QTableWidgetItem(comment[str_to_qstr('status')]))
                self.ui.tblComments.setItem(row, 3, QtGui.QTableWidgetItem(comment[str_to_qstr('author')]))
                self.ui.tblComments.setItem(row, 4, QtGui.QTableWidgetItem(comment[str_to_qstr('content')][:100]+'...'))
                self.ui.tblComments.setItem(row, 5, QtGui.QTableWidgetItem(comment[str_to_qstr('post_title')]))
                row += 1
            self.ui.tblComments.resizeColumnsToContents()

    def display_errmsg(self, msg):
        QtGui.QMessageBox.warning(self, 'Warning!', msg, QtGui.QMessageBox.Ok)

    def update_status(self, status):
        self.ui.statusLabel.setText(status)

    def update_progressbar(self, loading):
        if loading:
            self.ui.progressBar.show()
        else:
            self.ui.progressBar.hide()

    def showConfigWindow(self):
        self.settings.pull_data()
        self.settings.exec_()

    def showAboutWindow(self):
        aboutWindow = AboutWindow()
        aboutWindow.exec_()

