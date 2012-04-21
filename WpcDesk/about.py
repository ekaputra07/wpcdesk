# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from gui.about_window import Ui_AboutWindow

class AboutWindow(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

