# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wallet.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wallet(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 388)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

        Dialog.setWindowIcon(QtGui.QIcon("img/wallet_icon.png"))
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 120, 471, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_bath50 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath50.setGeometry(QtCore.QRect(40, 70, 93, 28))
        self.btn_bath50.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.btn_bath50.setObjectName("btn_bath50")
        self.btn_bath100 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath100.setGeometry(QtCore.QRect(190, 70, 93, 28))
        self.btn_bath100.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btn_bath100.setObjectName("btn_bath100")
        self.btn_bath249 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath249.setGeometry(QtCore.QRect(340, 70, 93, 28))
        self.btn_bath249.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_bath249.setObjectName("btn_bath249")
        self.btn_bath359 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath359.setGeometry(QtCore.QRect(40, 170, 93, 28))
        self.btn_bath359.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.btn_bath359.setObjectName("btn_bath359")
        self.btn_bath699 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath699.setGeometry(QtCore.QRect(190, 170, 93, 28))
        self.btn_bath699.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.btn_bath699.setObjectName("btn_bath699")
        self.btn_bath1050 = QtWidgets.QPushButton(self.groupBox)
        self.btn_bath1050.setGeometry(QtCore.QRect(340, 170, 93, 28))
        self.btn_bath1050.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_bath1050.setObjectName("btn_bath1050")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lbl_top = QtWidgets.QLabel(Dialog)
        self.lbl_top.setGeometry(QtCore.QRect(130, 60, 221, 16))
        self.lbl_top.setObjectName("lbl_top")

        self.lbl_id = QtWidgets.QLabel(Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(450, 60, 55, 16))
        self.lbl_id.setObjectName("lbl_id")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wallet"))
        self.label.setText(_translate("Dialog", "Topup Money"))
        self.groupBox.setTitle(_translate("Dialog", "เลือกราคาที่จะเติม"))
        self.btn_bath50.setText(_translate("Dialog", "50 Bath"))
        self.btn_bath100.setText(_translate("Dialog", "100 Bath"))
        self.btn_bath249.setText(_translate("Dialog", "249 Bath"))
        self.btn_bath359.setText(_translate("Dialog", "359 Bath"))
        self.btn_bath699.setText(_translate("Dialog", "699 Bath"))
        self.btn_bath1050.setText(_translate("Dialog", "1050 Bath"))
        self.label_2.setText(_translate("Dialog", "Wallet:"))
        self.lbl_top.setText(_translate("Dialog", "TextLabel"))
        # self.lbl_id.setText(_translate("Dialog", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_wallet()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

