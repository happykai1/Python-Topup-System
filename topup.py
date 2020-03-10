# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class topup(object):



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(725, 354)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

        Dialog.setWindowIcon(QtGui.QIcon("img/main_icon.png"))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 101))
        res = self.label.setPixmap(QtGui.QPixmap('img/client.png'))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 210, 141, 71))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 210, 141, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 0);")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 40, 91, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 85, 0);")

        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 80, 93, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        # self.label.setText(_translate("Dialog", "Pic User"))
        self.label_2.setText(_translate("Dialog", "UserID: "))
        # self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "TopUpWallet"))
        self.pushButton_2.setText(_translate("Dialog", "Game"))
        self.pushButton_3.setText(_translate("Dialog", "History"))
        self.pushButton_4.setText(_translate("Dialog", "Logout"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = topup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

