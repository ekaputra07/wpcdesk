# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Wed Feb  1 00:26:33 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_formConfig(object):
    def setupUi(self, formConfig):
        formConfig.setObjectName("formConfig")
        formConfig.setWindowModality(QtCore.Qt.ApplicationModal)
        formConfig.resize(362, 168)
        self.gridLayout = QtGui.QGridLayout(formConfig)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(formConfig)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(formConfig)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(formConfig)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.serverEdit = QtGui.QLineEdit(formConfig)
        self.serverEdit.setObjectName("serverEdit")
        self.verticalLayout.addWidget(self.serverEdit)
        self.usernameEdit = QtGui.QLineEdit(formConfig)
        self.usernameEdit.setObjectName("usernameEdit")
        self.verticalLayout.addWidget(self.usernameEdit)
        self.passEdit = QtGui.QLineEdit(formConfig)
        self.passEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passEdit.setAutoFillBackground(False)
        self.passEdit.setInputMask("")
        self.passEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.verticalLayout.addWidget(self.passEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.btnClose = QtGui.QPushButton(formConfig)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.btnClose, 1, 0, 1, 1)
        self.btnSave = QtGui.QPushButton(formConfig)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 1, 1, 1, 1)

        self.retranslateUi(formConfig)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), formConfig.close)
        QtCore.QMetaObject.connectSlotsByName(formConfig)

    def retranslateUi(self, formConfig):
        formConfig.setWindowTitle(QtGui.QApplication.translate("formConfig", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formConfig", "XML-RPC Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("formConfig", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("formConfig", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("formConfig", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("formConfig", "Save", None, QtGui.QApplication.UnicodeUTF8))

