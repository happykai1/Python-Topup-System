# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo

class Ui_register(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def signup(self):
        username_info = self.lineEdit.text()
        password_info = self.lineEdit_2.text()
        email_info = self.lineEdit_3.text()
        phone_info = self.lineEdit_4.text()

        if len(username_info) > 0 and len(password_info) > 0 and len(email_info) > 0 and (
                phone_info.isdigit() and len(phone_info) == 10):
            phone = [phone_info[0:2]]
            check = ['06', '09']
            pcheck = set(phone) & set(check)
            if pcheck:
                conn = pymongo.MongoClient("localhost", 27017)
                db = conn.get_database("shop_game")
                result = db.user.find({"userid": username_info}).count()
                result2 = db.user.find({"email": email_info}).count()
                if result == 0 and result2 ==0:
                    res = db.user.insert_many([{"userid": "{0}".format(username_info),
                                                "password": "{0}".format(password_info), "email": "{0}".format(email_info),
                                                "phone": "{0}".format(phone_info),"wallet":0}])
                    self.messagebox("Success", "You have been successfully registered")
                    conn.close()
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
                    self.lineEdit_3.clear()
                    self.lineEdit_4.clear()
                else:
                    if result ==1 and result2 ==0:
                        self.messagebox("Sorry", "UserID already exists")
                    elif result2 ==1 and result ==0:
                        self.messagebox("Sorry", "Email already exists")
                    elif result ==1 and result2 ==1:
                        self.messagebox("Sorry", "UserID / Email already exists")
                    conn.close()
            else:
                self.messagebox("Sorry", "The phone number must start with 06 or 09")
        else:
            self.messagebox("Sorry", "Please enter details below")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 424)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        Dialog.setWindowIcon(QtGui.QIcon("img/regis_icon.png"))
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 290, 111, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 127);")

        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.signup)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 230, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(360, 110, 113, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 150, 113, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 190, 113, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 230, 113, 22))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setMaxLength(10)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))
        self.label.setText(_translate("Dialog", "UserID"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "E-mail"))
        self.label_4.setText(_translate("Dialog", "Phone <br>(e.g.,06xxxxxxxx)"))
        self.label_5.setText(_translate("Dialog", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_register()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

