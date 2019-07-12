# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ebook.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(467, 172)
        self.label = QtWidgets.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GroupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(GroupBox)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 80, 113, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "抓取设置"))
        self.label.setText(_translate("GroupBox", "请选择抓取期数："))
        self.label_2.setText(_translate("GroupBox", "请选择保存路径："))
        self.label_3.setText(_translate("GroupBox", "期数范围（01-24）"))
        self.pushButton.setText(_translate("GroupBox", "选择"))
