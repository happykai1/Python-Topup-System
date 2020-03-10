from PyQt5 import QtCore, QtGui, QtWidgets

from loginV3 import Ui_MainWindow
from topup import topup
from register import Ui_register
from wallet import Ui_wallet
from game import Ui_game
from history import Ui_history
import pymongo ,csv,datetime
import sys

class topup(QtWidgets.QDialog, topup):
    def __init__(self, text, parent=None):
        super(topup, self).__init__(parent)
        self.setupUi(self)
        # self.lineEdit.setText(text)
        self.label_3.setText(text)
        self.pushButton.clicked.connect(self.opentopwallet)
        self.pushButton_2.clicked.connect(self.opentogame)
        self.pushButton_3.clicked.connect(self.openhistory)
        self.pushButton_4.clicked.connect(self.logout)


    def logout(self):
        self.close()
        main()

    def opentopwallet(self):
        uid = self.label_3.text()
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("shop_game")
        result = db.user.find({"userid":uid})
        conn.close()
        p=[result[0]['userid'], result[0]['wallet']]
        wa = wallet(p)
        wa.exec_()

    def opentogame(self):
        uid = self.label_3.text()
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("shop_game")
        result = db.user.find({"userid": uid})
        conn.close()
        p = [result[0]['userid'], result[0]['wallet']]
        g = game(p)
        g.exec_()

    def openhistory(self):
        uid = self.label_3.text()
        h = history(uid)
        h.exec_()


class wallet(QtWidgets.QDialog,Ui_wallet):
    def __init__(self, text, parent=None):
        super(wallet, self).__init__(parent)
        self.setupUi(self)
        self.lbl_id.setText(str(text[0]))
        self.lbl_id.hide()
        self.lbl_top.setText(str(text[1])+" Baths")
        self.btn_bath50.clicked.connect(self.insertwallet_50)
        self.btn_bath100.clicked.connect(self.insertwallet_100)
        self.btn_bath249.clicked.connect(self.insertwallet_249)
        self.btn_bath359.clicked.connect(self.insertwallet_359)
        self.btn_bath699.clicked.connect(self.insertwallet_699)
        self.btn_bath1050.clicked.connect(self.insertwallet_1050)

    def insertwallet_50(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+50
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                  "Type": "{0}".format("Topup"), "Money": 50,
                                  "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

    def insertwallet_100(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+100
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                     "Type": "{0}".format("Topup"), "Money": 100,
                                     "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

    def insertwallet_249(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+249
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                     "Type": "{0}".format("Topup"), "Money": 249,
                                     "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

    def insertwallet_359(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+359
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                     "Type": "{0}".format("Topup"), "Money": 359,
                                     "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

    def insertwallet_699(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+699
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                     "Type": "{0}".format("Topup"), "Money": 699,
                                     "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

    def insertwallet_1050(self):
        uid =  self.lbl_id.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            price = int(result[0]['wallet'])+1050
            db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
            db.history.insert_many([{"userid": "{0}".format(uid),
                                     "Type": "{0}".format("Topup"), "Money": 1050,
                                     "Into": "{0}".format("wallet")}])
            conn.close()
            self.lbl_top.setText(str(price)+" Baths")
            self.update()
        else:
            print("No")

class game(QtWidgets.QDialog,Ui_game):
    def __init__(self, text,parent=None):
        super(game, self).__init__(parent)
        self.setupUi(self)
        self.lbl_gid.setText(str(text[0]))
        self.lbl_gid.hide()
        self.lbl_price.setText(str(text[1])+" Baths")
        self.btn_rov50.clicked.connect(self.toprov_50)
        self.btn_rov349.clicked.connect(self.toprov_349)
        self.btn_rov500.clicked.connect(self.toprov_500)
        self.btn_on179.clicked.connect(self.topon_179)
        self.btn_on349.clicked.connect(self.topon_349)
        self.btn_on1050.clicked.connect(self.topon_1050)

    def toprov_50(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=50:
                price = int(result[0]['wallet'])-50
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 50,
                                         "Into": "{0}".format("ROV")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

    def toprov_349(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=349:
                price = int(result[0]['wallet'])-349
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 349,
                                         "Into": "{0}".format("ROV")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

    def toprov_500(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=500:
                price = int(result[0]['wallet'])-500
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 500,
                                         "Into": "{0}".format("ROV")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

    def topon_179(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=179:
                price = int(result[0]['wallet'])-179
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 179,
                                         "Into": "{0}".format("Onmyoji")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

    def topon_349(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=349:
                price = int(result[0]['wallet'])-349
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 349,
                                         "Into": "{0}".format("Onmyoji")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

    def topon_1050(self):
        uid =  self.lbl_gid.text()
        mess = QtWidgets.QMessageBox
        msgbox = mess.question(self, "Confirm", "Are you sure you want to topup?", mess.Yes | mess.No,mess.No)
        if msgbox == QtWidgets.QMessageBox.Yes:
            conn = pymongo.MongoClient("localhost", 27017)
            db = conn.get_database("shop_game")
            result = db.user.find({"userid": uid})
            if int(result[0]['wallet']) >=1050:
                price = int(result[0]['wallet'])-1050
                db.user.update_one({"userid": uid},{"$set":{"wallet":price}})
                db.history.insert_many([{"userid": "{0}".format(uid),
                                         "Type": "{0}".format("Buy"), "Money": 1050,
                                         "Into": "{0}".format("Onmyoji")}])
                conn.close()
                self.lbl_price.setText(str(price)+" Baths")
                self.update()
            else:
                self.warning("Fail", "Please Topup")
        else:
            print("No")

class history(QtWidgets.QDialog,Ui_history):
    def __init__(self, text,parent=None):
        super(history, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(text)
        self.label.hide()
        self.pushButton.clicked.connect(self.LoadData)
        self.pushButton_2.clicked.connect(self.ExportData)


    def LoadData(self):
        uid = self.label.text()
        type = self.comboBox.currentText()
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("shop_game")
        if type != "Both":
            result = db.history.find({"userid":uid,"Type":type})
        else:
            result = db.history.find({"userid": uid})
        conn.close()
        list2 = []
        for i in result:
            list = []
            list.append(i['userid'])
            list.append(i['Type'])
            list.append(i['Money'])
            list.append(i['Into'])
            list2.append(list)
        self.tableWidget.setRowCount(0)

        for row_number , row_data in enumerate(list2):
            self.tableWidget.insertRow(row_number)
            for column_num,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_num,QtWidgets.QTableWidgetItem(str(data)))

    def ExportData(self):
        now = datetime.datetime.now()
        x = now.strftime("%Y-%m-%d-%H-%M-%S")
        uid = self.label.text()
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("shop_game")
        result = db.history.find({"userid": uid})
        conn.close()
        list2 = []
        for i in result:
            list = []
            list.append(i['userid'])
            list.append(i['Type'])
            list.append(i['Money'])
            list.append(i['Into'])
            list2.append(list)
        with open("LogData/Log_"+uid+"-"+x+".csv",'w',newline='',encoding="UTF-8") as f:
            fw = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            fw.writerows(list2)
        self.messagebox("Success","Export data Done!")

class register(QtWidgets.QDialog, Ui_register):
    def __init__(self, parent=None):
        super(register, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.logintotopup)
        # self.pushButton.clicked.connect(self.openDialog)
        self.pushButton_2.clicked.connect(self.openWindowRegister)

    def logintotopup(self):
        username=self.lineEdit.text()
        password = self.lineEdit_2.text()
        conn = pymongo.MongoClient("localhost", 27017)
        db = conn.get_database("shop_game")
        result = db.user.find({"userid": username, "password": password})
        conn.close()
        if result.count() > 0:
            self.messagebox("Success ","Logged in")
            # data = self.label_4.text()
            data = result[0]['userid']
            self.hide()
            w = topup(data)
            w.exec_()
        else:
            self.warning("Fail","Username / Password is not correct")

    def openWindowRegister(self):
        r = register()
        r.exec_()

def main():
    global w
    w = MainWindow()
    w.show()
    return w
    # sys.exit(app.exec_())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    app.exec_()

