# -*- coding: utf-8 -*-

import sys
import time
import xmlrpclib
from PyQt4 import QtGui, QtCore
from gui.main_window import Ui_mainWindow
from settings import ConnectionSettings
from about import AboutWindow
from comment_editor import CommentEditor
from wpcdesk_threads import GetCommentsThread
from utils import str_to_qstr


class wpcDesk(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.settings = ConnectionSettings()

        QtCore.QObject.connect(self.ui.actionRefresh, QtCore.SIGNAL("activated()"), self.loadComments)
        QtCore.QObject.connect(self.ui.actionConnection, QtCore.SIGNAL("activated()"), self.showConfigWindow)
        QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("activated()"), self.showAboutWindow)
        QtCore.QObject.connect(self.ui.tblComments, QtCore.SIGNAL("itemDoubleClicked(QTableWidgetItem*)"), self.showCommentEditor)

        self.get_comments_thread = GetCommentsThread()
        self.get_comments_thread.response_received.connect(self.display_comments)
        self.get_comments_thread.error_raised.connect(self.display_errmsg)
        self.get_comments_thread.is_loading.connect(self.update_progressbar)
        self.get_comments_thread.status_updated.connect(self.update_status)

        if not self.settings.is_config_exists:
            self.update_status('Connection settings not available!')
        else:
            self.update_status('Ready to connect...')

        self.ui.progressBar.hide()
        self.loadComments()


    def loadComments(self):
        if not self.settings.is_config_exists:
            QtGui.QMessageBox.warning(self, 'Warning!','Connection settings not available!', QtGui.QMessageBox.Ok)
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

                datetime = QtGui.QTableWidgetItem()
                datetime.setText(date)
                datetime.setIcon(QtGui.QIcon(':/time.png'))
                self.ui.tblComments.setItem(row, 1, datetime)

                #set status
                status = QtGui.QTableWidgetItem()
                if comment[str_to_qstr('status')] == 'approve':
                    s = 'Approved'
                    icon = QtGui.QIcon(':/tick.png')
                else:
                    s = 'Pending'
                    icon = QtGui.QIcon(':/cross.png')

                status.setText(s)
                status.setIcon(icon)
                self.ui.tblComments.setItem(row, 2, status)

                #set author
                author = QtGui.QTableWidgetItem()
                author.setText(comment[str_to_qstr('author')])
                author.setIcon(QtGui.QIcon(':/user.png'))
                self.ui.tblComments.setItem(row, 3, author)

                #set email
                self.ui.tblComments.setItem(row, 4, QtGui.QTableWidgetItem(comment[str_to_qstr('author_email')]))

                #set comment
                comm = QtGui.QTableWidgetItem()
                comm.setText(comment[str_to_qstr('content')])
                comm.setIcon(QtGui.QIcon(':/comment.png'))
                self.ui.tblComments.setItem(row, 5, comm)

                self.ui.tblComments.setItem(row, 6, QtGui.QTableWidgetItem(comment[str_to_qstr('post_title')]))

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

    def showCommentEditor(self, QTableWidgetItem):
        row = QTableWidgetItem.row()

        data = {
        'comment_id': self.ui.tblComments.item(row, 0).text(),
        'comment_date': self.ui.tblComments.item(row, 1).text(),
        'comment_status': self.ui.tblComments.item(row, 2).text(),
        'comment_author': self.ui.tblComments.item(row, 3).text(),
        'comment_email': self.ui.tblComments.item(row, 4).text(),
        'comment_content': self.ui.tblComments.item(row, 5).text(),
        'comment_post': self.ui.tblComments.item(row, 6).text(),
        }

        commentWindow = CommentEditor(parent=self, data=data)
        commentWindow.exec_()

