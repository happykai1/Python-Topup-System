# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_history(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 475)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

        Dialog.setWindowIcon(QtGui.QIcon("img/history_icon.png"))

        Dialog.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 390, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(200, 200, 181);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 390, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 200, 181);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 350, 55, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 70, 511, 261))
        self.tableWidget.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"selection-background-color: rgb(170, 255, 127);")
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(480, 20, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 25, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(85, 85, 0);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "History"))
        self.pushButton.setText(_translate("Dialog", "Load"))
        self.pushButton_2.setText(_translate("Dialog", "Export"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Userid"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Money"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Into"))
        self.comboBox.setCurrentText(_translate("Dialog", "Buy"))
        self.comboBox.setItemText(0, _translate("Dialog", "Buy"))
        self.comboBox.setItemText(1, _translate("Dialog", "Topup"))
        self.comboBox.setItemText(2, _translate("Dialog", "Both"))
        self.label_2.setText(_translate("Dialog", "Select Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_history()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

