#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from main import wpcDesk


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wpcdesk = wpcDesk()
    wpcdesk.showMaximized()
    sys.exit(app.exec_())

