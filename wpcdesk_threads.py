# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import xmlrpclib

from settings import get_connection_settings

class GetCommentsThread(QtCore.QThread):

    response_received = QtCore.pyqtSignal(list)
    error_raised = QtCore.pyqtSignal(str)

    #connection_settings = ConnectionSettings()

    def run(self):
        data = get_connection_settings()
        server_url = str(data.get('server', ''))
        username = str(data.get('username', ''))
        password = str(data.get('password', ''))

        server = xmlrpclib.Server(server_url)
        extra = {'number':20}
        try:
            comments = server.wp.getComments(1, username, password, extra)
            self.response_received.emit(comments)
        except:
            self.error_raised.emit('Failed connecting to server,\nMake sure connection setting is correct.')

