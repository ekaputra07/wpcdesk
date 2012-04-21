# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sun Apr 22 00:42:55 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_formConfig(object):
    def setupUi(self, formConfig):
        formConfig.setObjectName("formConfig")
        formConfig.setWindowModality(QtCore.Qt.ApplicationModal)
        formConfig.resize(465, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formConfig.sizePolicy().hasHeightForWidth())
        formConfig.setSizePolicy(sizePolicy)
        formConfig.setMinimumSize(QtCore.QSize(465, 200))
        formConfig.setMaximumSize(QtCore.QSize(465, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/chat-quotes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formConfig.setWindowIcon(icon)
        self.btnClose = QtGui.QPushButton(formConfig)
        self.btnClose.setGeometry(QtCore.QRect(260, 160, 85, 27))
        self.btnClose.setObjectName("btnClose")
        self.btnSave = QtGui.QPushButton(formConfig)
        self.btnSave.setGeometry(QtCore.QRect(360, 160, 85, 27))
        self.btnSave.setObjectName("btnSave")
        self.widget = QtGui.QWidget(formConfig)
        self.widget.setGeometry(QtCore.QRect(9, 9, 441, 141))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.serverEdit = QtGui.QLineEdit(self.widget)
        self.serverEdit.setObjectName("serverEdit")
        self.verticalLayout.addWidget(self.serverEdit)
        self.usernameEdit = QtGui.QLineEdit(self.widget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.verticalLayout.addWidget(self.usernameEdit)
        self.passEdit = QtGui.QLineEdit(self.widget)
        self.passEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passEdit.setAutoFillBackground(False)
        self.passEdit.setInputMask("")
        self.passEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.verticalLayout.addWidget(self.passEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(formConfig)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), formConfig.close)
        QtCore.QMetaObject.connectSlotsByName(formConfig)

    def retranslateUi(self, formConfig):
        formConfig.setWindowTitle(QtGui.QApplication.translate("formConfig", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("formConfig", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("formConfig", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formConfig", "XML-RPC Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("formConfig", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("formConfig", "Password", None, QtGui.QApplication.UnicodeUTF8))

import main_rc
