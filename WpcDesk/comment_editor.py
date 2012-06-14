# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from gui.comment_window import Ui_CommentWindow
from wpcdesk_threads import EditCommentThread

class CommentEditor(QtGui.QDialog):

    def __init__(self, parent=None, data=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CommentWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.hide()
        self.set_validator()
        self.parent = parent

        self.data = data
        self.fill_form(self.data)

        QtCore.QObject.connect(self.ui.btn_save, QtCore.SIGNAL("clicked()"), self.saveComment)

        self.edit_comment_thread = EditCommentThread()
        self.edit_comment_thread.is_loading.connect(self.edit_loading)
        self.edit_comment_thread.is_success.connect(self.edit_status)

    def set_validator(self):
        # Email Validator
        email_pattern = QtCore.QRegExp( r"^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$" )
        email_validator = QtGui.QRegExpValidator(email_pattern , self )
        self.ui.edit_email.setValidator(email_validator)

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

    def saveComment(self):
        data = {}
        if self.ui.cb_status.isChecked():
            data['status'] = 'approve'
        else:
            data['status'] = 'hold'
        data['content'] = str(self.ui.edit_comment.toPlainText())
        data['author'] = str(self.ui.edit_name.text())
        data['author_email'] = str(self.ui.edit_email.text())

        self.edit_comment_thread.set_comment_id(int(self.data['comment_id']))
        self.edit_comment_thread.set_data(data)
        self.edit_comment_thread.start()

    def edit_loading(self, is_loading):
        if is_loading:
            self.ui.progressBar.show()
        else:
            self.ui.progressBar.hide()

    def edit_status(self, status):
        if status:
            self.parent.loadComments()
            QtGui.QMessageBox.information(self, 'Comment updated!','Comment successfuly updated.', QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.warning(self, 'Failed!','Failed to update comment.', QtGui.QMessageBox.Ok)

