# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import xmlrpclib

from settings import get_connection_settings

class BaseCommentThread(QtCore.QThread):
    """
    The base thread class for all connection thread used by this application.
    """
    connection_error_status = 'Connection error...'
    connection_error_msg = 'Failed connecting to server,\nMake sure connection settings is correct and you are connected to internet.'

    def get_connection(self):
        data = get_connection_settings()
        self.server_url = str(data.get('server', ''))
        self.server = xmlrpclib.Server(self.server_url)
        self.username = str(data.get('username', ''))
        self.password = str(data.get('password', ''))


class GetCommentsThread(BaseCommentThread):
    """ Get latest comments """

    response_received = QtCore.pyqtSignal(list)
    error_raised = QtCore.pyqtSignal(str)
    status_updated = QtCore.pyqtSignal(str)
    is_loading = QtCore.pyqtSignal(bool)

    def run(self):
        self.get_connection()
        self.is_loading.emit(True)
        extra = {'number':20}
        try:
            self.status_updated.emit('Connecting to %s...' % self.server_url)
            comments = self.server.wp.getComments(1, self.username, self.password, extra)
        except:
            self.is_loading.emit(False)
            self.status_updated.emit(self.connection_error_status)
            self.error_raised.emit(self.connection_error_msg)
        else:
            comments_num = len(comments)
            self.status_updated.emit('%s comments received.' % str(comments_num))
            self.response_received.emit(comments)
            self.is_loading.emit(False)


class EditCommentThread(BaseCommentThread):
    """ Edit single comment """

    is_loading = QtCore.pyqtSignal(bool)
    is_success = QtCore.pyqtSignal(bool)

    def set_data(self, data):
        self.data = data

    def set_comment_id(self, comment_id):
        self.comment_id = comment_id

    def run(self):
        self.get_connection()
        self.is_loading.emit(True)
        try:
            status = self.server.wp.editComment(1, self.username, self.password, self.comment_id, self.data)
        except:
            self.is_success.emit(False)
        else:
            self.is_success.emit(True)

        self.is_loading.emit(False)

class DeleteCommentThread(BaseCommentThread):
    """ Delete comment """

    is_loading = QtCore.pyqtSignal(bool)
    is_success = QtCore.pyqtSignal(bool)

    def __init__(self, data, *args, **kwargs):
        super(DeleteCommentThread, self).__init__(*args, **kwargs)
        self.comment_id = data['comment_id']

    def run(self):
        self.get_connection()
        self.is_loading.emit(True)
        try:
            status = self.server.wp.deleteComment(1, self.username, self.password, int(self.comment_id))
        except:
            self.is_success.emit(False)
        else:
            self.is_success.emit(True)

        self.is_loading.emit(False)
