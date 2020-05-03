# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_select.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_select(object):
    def setupUi(self, select):
        select.setObjectName("select")
        select.resize(580, 310)
        select.setMinimumSize(QtCore.QSize(580, 310))
        select.setMaximumSize(QtCore.QSize(580, 310))
        select.setStyleSheet("backgroud_color:rgb(255, 255, 255)")
        self.easy = QtWidgets.QPushButton(select)
        self.easy.setGeometry(QtCore.QRect(70, 120, 103, 103))
        self.easy.setStyleSheet("background-image:url(:/images/source/easy100.png)")
        self.easy.setText("")
        self.easy.setObjectName("easy")
        self.normal = QtWidgets.QPushButton(select)
        self.normal.setGeometry(QtCore.QRect(240, 120, 103, 103))
        self.normal.setStyleSheet("background-image:url(:/images/source/normal100.png)")
        self.normal.setText("")
        self.normal.setObjectName("normal")
        self.hard = QtWidgets.QPushButton(select)
        self.hard.setGeometry(QtCore.QRect(410, 120, 103, 103))
        self.hard.setStyleSheet("background-image:url(:/images/source/hard100.png)")
        self.hard.setText("")
        self.hard.setObjectName("hard")
        self.label = QtWidgets.QLabel(select)
        self.label.setGeometry(QtCore.QRect(170, 20, 240, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(select)
        self.label_2.setGeometry(QtCore.QRect(70, 235, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(select)
        self.label_3.setGeometry(QtCore.QRect(240, 235, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(select)
        self.label_4.setGeometry(QtCore.QRect(410, 235, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("select", "难度选择"))
        self.label.setText(_translate("select", "难 度 选 择"))
        self.label_2.setText(_translate("select", "简  单"))
        self.label_3.setText(_translate("select", "一  般"))
        self.label_4.setText(_translate("select", "困  难"))

import images
