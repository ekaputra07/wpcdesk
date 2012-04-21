# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import xmlrpclib

from settings import get_connection_settings

class GetCommentsThread(QtCore.QThread):

    response_received = QtCore.pyqtSignal(list)
    error_raised = QtCore.pyqtSignal(str)
    status_updated = QtCore.pyqtSignal(str)
    is_loading = QtCore.pyqtSignal(bool)

    def run(self):
        self.is_loading.emit(True)
        data = get_connection_settings()
        server_url = str(data.get('server', ''))
        username = str(data.get('username', ''))
        password = str(data.get('password', ''))

        server = xmlrpclib.Server(server_url)
        extra = {'number':20}
        try:
            self.status_updated.emit('Connecting to %s...' % server_url)
            comments = server.wp.getComments(1, username, password, extra)
            comments_num = len(comments)
            self.status_updated.emit('%s comments received.' % str(comments_num))
            self.response_received.emit(comments)
            self.is_loading.emit(False)
        except:
            self.is_loading.emit(False)
            self.status_updated.emit('Connection error...')
            self.error_raised.emit('Failed connecting to server,\nMake sure connection settings is correct.')

