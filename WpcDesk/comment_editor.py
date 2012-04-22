# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gui.comment_window import Ui_CommentWindow

class CommentEditor(QtGui.QDialog):

    def __init__(self, parent=None, data=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CommentWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()

        self.data = data
        self.fill_form(self.data)

    def fill_form(self, data):
        self.comment_id = data['comment_id']

        self.ui.lbl_post.setText(data['comment_post'])
        self.ui.lbl_date.setText(data['comment_date'])
        self.ui.edit_name.setText(data['comment_author'])
        self.ui.edit_email.setText(data['comment_email'])
        self.ui.edit_comment.setText(data['comment_content'])

        if data['comment_status'] == 'Approved':
            self.ui.cb_status.setChecked(True)
        else:
            self.ui.cb_status.setChecked(False)

