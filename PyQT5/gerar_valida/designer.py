# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 153)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 25, 90, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(7, 100, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.inputValidar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValidar.setGeometry(QtCore.QRect(100, 26, 231, 27))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.inputValidar.setFont(font)
        self.inputValidar.setObjectName("inputValidar")
        self.btnValidar = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidar.setGeometry(QtCore.QRect(347, 25, 120, 29))
        self.btnValidar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnValidar.setFont(font)
        self.btnValidar.setObjectName("btnValidar")
        self.btnGerar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerar.setGeometry(QtCore.QRect(350, 100, 120, 29))
        self.btnGerar.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnGerar.setFont(font)
        self.btnGerar.setObjectName("btnGerar")
        self.labelValida = QtWidgets.QLabel(self.centralwidget)
        self.labelValida.setGeometry(QtCore.QRect(100, 60, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelValida.setFont(font)
        self.labelValida.setText("")
        self.labelValida.setObjectName("labelValida")
        self.labelGerar = QtWidgets.QLabel(self.centralwidget)
        self.labelGerar.setGeometry(QtCore.QRect(100, 100, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelGerar.setFont(font)
        self.labelGerar.setText("")
        self.labelGerar.setObjectName("labelGerar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validar Gerar CPF"))
        self.label.setText(_translate("MainWindow", "Validar CPF:"))
        self.label_2.setText(_translate("MainWindow", "Gerar CPF:"))
        self.btnValidar.setText(_translate("MainWindow", "Validar"))
        self.btnGerar.setText(_translate("MainWindow", "Gerar"))
