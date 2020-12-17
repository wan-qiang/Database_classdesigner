import pymysql
from PyQt5 import *
import sys
from PyQt5.QtWidgets import *
from login_proprietor import *
from login import *
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='ssh_crud',
    charset='utf8')
cursor = conn.cursor()

def sql_login(a, b):

    value1 = (a,)
    value2 = (b,)
    table = ['admin','family_account_number','staff_account_number']
    flag = 0
    sql1 = "select id from admin"
    sql2 = "select id from family_account_number"
    sql3 = "select id from staff_account_number"
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()
    for myret1 in ret1:
        if value1 == myret1:
            flag = 1
            break
    if flag == 0:
        for myret2 in ret2:
            if value1 == myret2:
                flag = 2
                break
    if flag == 0:
        for myret3 in ret3:
            if value1 == myret3:
                flag = 3
                break
    sql4 = "select password from " + table[flag-1] + " where(id = \'" + a + "\');"
    cursor.execute(sql4)
    ret = cursor.fetchone()

    conn.commit()
    if flag == 0:
        return 0
    if value2 == ret:
        return 2
    else:
        return 1



# def switch_window():#退出主窗口，打开副窗口
#     ui2.show()
#     ui1.hide()
#
# class first_window(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.first = Ui_login()
#         self.first.setupUi(self)
#         def test_login():
#             text1 = self.first.lineEdit.text()
#             text2 = self.first.lineEdit_2.text()
#             x = sql_login(text1, text2)
#             print(x)
#             if x == 2:
#                 switch_window()
#             else:
#                 QtWidgets.QMessageBox.critical(ui1, '错误', '用户名或密码错误')
#
#         self.first.pushButton.clicked.connect(test_login)
#         self.first.pushButton_3.clicked.connect(exit)
#
# class second_Window(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.second = Ui_proprietor()
#         self.second.setupUi(self)
#
#
# app = QtWidgets.QApplication(sys.argv)
# ui1 = first_window()
# ui2 = second_Window()
# ui1.show()
# sys.exit(app.exec_())
# conn.close()

def sql_change_password(a, b, c, d):
    cursor = conn.cursor()
    value1 = (a,)
    value2 = (b,)
    value3 = (c,)
    value4 = (d,)
    table_number = 0
    table = ['admin', 'family_account_number', 'staff_account_number']
    sql1 = "select id from admin"
    sql2 = "select id from family_account_number"
    sql3 = "select id from staff_account_number"

    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()

    for myret1 in ret1:
        if value1 == myret1 :
            table_number = 1
            break
    if table_number == 0:
        for myret2 in ret2:
            if value1 == myret2:
                table_number = 2
                break
    if table_number == 0:
        for myret3 in ret3:
            if value1 == myret3:
                table_number = 3
                break

    sql4 = "select password from " + table[table_number-1] + " where(id = \'" + a + "\');"

    cursor.execute(sql4)
    ret = cursor.fetchone()

    sql5 = "update " + table[table_number - 1] + " set password = \'" + c + "\' where id = \'" + a + "\';"


    if table_number == 0 :
        return 0 #用户名不存在
    if value2 != ret:
        return 1#密码错误
    if value2 == ret :
        if value3 == value4 :
            cursor.execute(sql5)
            conn.commit()
            return 3 #修改成功
        else:
            return 2 #密码不一致
