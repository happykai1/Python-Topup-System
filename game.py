# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_game(object):
    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 385)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

        Dialog.setWindowIcon(QtGui.QIcon("img/game_icon.png"))
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 110, 211, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_rov50 = QtWidgets.QPushButton(self.groupBox)
        self.btn_rov50.setGeometry(QtCore.QRect(60, 50, 93, 28))
        self.btn_rov50.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.btn_rov50.setObjectName("btn_rov50")
        self.btn_rov349 = QtWidgets.QPushButton(self.groupBox)
        self.btn_rov349.setGeometry(QtCore.QRect(60, 130, 93, 28))
        self.btn_rov349.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.btn_rov349.setObjectName("btn_rov349")
        self.btn_rov500 = QtWidgets.QPushButton(self.groupBox)
        self.btn_rov500.setGeometry(QtCore.QRect(60, 210, 93, 28))
        self.btn_rov500.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.btn_rov500.setObjectName("btn_rov500")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 110, 211, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_on179 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_on179.setGeometry(QtCore.QRect(60, 50, 93, 28))
        self.btn_on179.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btn_on179.setObjectName("btn_on179")
        self.btn_on349 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_on349.setGeometry(QtCore.QRect(60, 130, 93, 28))
        self.btn_on349.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btn_on349.setObjectName("btn_on349")
        self.btn_on1050 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_on1050.setGeometry(QtCore.QRect(60, 210, 93, 28))
        self.btn_on1050.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btn_on1050.setObjectName("btn_on1050")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lbl_price = QtWidgets.QLabel(Dialog)
        self.lbl_price.setGeometry(QtCore.QRect(130, 60, 201, 16))
        self.lbl_price.setObjectName("lbl_price")
        self.lbl_gid = QtWidgets.QLabel(Dialog)
        self.lbl_gid.setGeometry(QtCore.QRect(460, 60, 55, 16))
        self.lbl_gid.setObjectName("lbl_gid")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Games"))
        self.groupBox.setTitle(_translate("Dialog", "RO_"))
        self.btn_rov50.setText(_translate("Dialog", "50 Shell"))
        self.btn_rov349.setText(_translate("Dialog", "349 Shell"))
        self.btn_rov500.setText(_translate("Dialog", "500 Shell"))
        self.groupBox_2.setTitle(_translate("Dialog", "Onmyoji Are_a"))
        self.btn_on179.setText(_translate("Dialog", "179 Diamond"))
        self.btn_on349.setText(_translate("Dialog", "349 Diamond"))
        self.btn_on1050.setText(_translate("Dialog", "1050 Diamond"))
        self.label.setText(_translate("Dialog", "Select Game"))
        self.label_2.setText(_translate("Dialog", "Wallet :"))
        self.lbl_price.setText(_translate("Dialog", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_game()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

