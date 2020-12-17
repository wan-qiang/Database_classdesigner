import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *

#from connect_mysql import *
import connect_mysql
from login import *
from login_proprietor import *
from change_password import *


def switch_window1():#打开业主界面,关闭登入界面
    ui_proprietor.show()
    ui_login.hide()

def switch_window2(): #打开修改密码界面，关闭登入界面
    ui_change_password.show()
    ui_login.hide()

def switch_window3(): #打开登入界面，关闭修改密码界面
    ui_login.show()
    ui_change_password.hide()

class login_window(QMainWindow): #继承login类
    def __init__(self):
        QMainWindow.__init__(self)
        self.login = Ui_login()
        self.login.setupUi(self)

        def test_login():   #检验登入过程
            text1 = self.login.lineEdit.text()
            text2 = self.login.lineEdit_2.text()
            x = connect_mysql.sql_login(text1, text2)
            print(x)
            if x == 2:
                switch_window1()
            else:
                QtWidgets.QMessageBox.critical(ui_login, '错误', '用户名或密码错误')

        self.login.pushButton.clicked.connect(test_login) # 敲击登入按钮
        self.login.pushButton_2.clicked.connect(switch_window2) #点击修改密码按钮
        self.login.pushButton_3.clicked.connect(exit)  #敲击退出系统按钮


class change_password_Window(QDialog):  # 继承Ui_change_password类
    def __init__(self):
        QDialog.__init__(self)
        self.change_password = Ui_change_password()
        self.change_password.setupUi(self)

        def test_change_password():  # 验证密码的正确性
            text1 = self.change_password.lineEdit.text()
            text2 = self.change_password.lineEdit_2.text()
            text3 = self.change_password.lineEdit_3.text()
            text4 = self.change_password.lineEdit_4.text()
            x = connect_mysql.sql_change_password(text1, text2, text3, text4)
            print(text4)
            print(x)
            if x == 3:
                print("修改成功")
                QMessageBox.information(ui_change_password, '修改密码', '修改密码成功，请继续下一步操作')

            elif x == 0 or x == 1:
                print("用户名或原密码错误")
                QtWidgets.QMessageBox.critical(ui_change_password, '错误', '用户名或原密码错误')

            elif x == 2:
                print("两次输入的密码不一致")
                QtWidgets.QMessageBox.critical(ui_change_password, '错误', '两次输入密码不一致')


        def incorrect_id_password():    #显示弹窗是否确定要修改密码
            reply = QtWidgets.QMessageBox.question(ui_change_password, '修改密码', '确定修改密码')
            if reply == QtWidgets.QMessageBox.Yes:
                print('yes')
                test_change_password()
            else:
                print('no')

        self.change_password.pushButton.clicked.connect(test_change_password)  # 显示确认是否修改密码弹窗
        #self.change_password.pushButton.clicked.connect(incorrect_id_password) #显示确认是否修改密码弹窗
        self.change_password.pushButton_2.clicked.connect(switch_window3)#从修改界面返回登入界面

class login_proprietor_Window(QDialog):  # 继承Ui_proprirtor类
    def __init__(self):
        QDialog.__init__(self)
        self.login_proprietor = Ui_proprietor()
        self.login_proprietor.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
ui_login = login_window()
ui_change_password = change_password_Window()
ui_proprietor = login_proprietor_Window()

ui_login.show()
sys.exit(app.exec_())

conn.close()
