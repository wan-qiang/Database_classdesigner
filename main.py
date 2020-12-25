import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import *

#from connect_mysql import *
import connect_mysql
from login import *
from change_password import *

from super_root import *
from super_root_inquery import *
from super_root_add_community import *

from root import *
from root_build import *
from root_car import *
from root_community import *
from root_family import *
from root_house_owner import *
from root_parking import *
from root_pet import *
from root_staff import *


from user import *
from user_car import *
from user_pet import *
from user_staff import *

login_data1 = 'x'
login_data2 = 'y'
community_id = 'z'

def switch_window1(): #打开超级管理员界面,关闭登入界面
    ui_super_root.show()
    ui_login.hide()

def switch_window2():#打开普通管理员界面，关闭登入界面
    ui_root.show()
    ui_login.hide()

def switch_window3():#打开业主界面,关闭登入界面
    ui_user.show()
    ui_login.hide()
    inquery_user_community()
    inquery_user_people()
    inquery_user_family()

def switch_window4(): #打开修改密码界面，关闭登入界面
    ui_change_password.show()
    ui_login.hide()

def switch_window5(): #打开登入界面，关闭修改密码界面
    ui_login.show()
    ui_change_password.change_password.lineEdit.clear()
    ui_change_password.change_password.lineEdit_2.clear()
    ui_change_password.change_password.lineEdit_3.clear()
    ui_change_password.change_password.lineEdit_4.clear()
    ui_change_password.hide()

def switch_window6():  #打开登入界面，关闭用户界面
    ui_login.show()
    ui_user.user.tableWidget.clearContents()
    ui_user.user.tableWidget_2.clearContents()
    ui_user.user.tableWidget_3.clearContents()
    ui_user.hide()

def switch_window7(): # 打开登入界面，关闭管理员界面
    ui_login.show()
    ui_root.hide()

def switch_window8(): #打开登入界面，关闭超级管理员界面
    ui_login.show()
    ui_super_root.super_root.lineEdit.clear()
    ui_super_root.super_root.tableWidget.clear()
    ui_super_root.hide()

def switch_window9():  # 打开添加小区界面，关闭超级管理员界面
    ui_super_root_add_community.show()
    ui_super_root.hide()

def switch_window10():  # 打开小区查询界面，关闭超级管理员界面
    ui_super_root_inquery.show()
    ui_super_root.hide()

def switch_window11():  # 打开超级管理员界面，关闭小区查询界面
    ui_super_root.show()
    ui_super_root_inquery.hide()

def switch_window12():  #打开超级管理员界面 ，关闭添加小区界面
    ui_super_root.show()
    ui_super_root_add_community.super_root_add_community.tableWidget.clearContents()
    ui_super_root_add_community.super_root_add_community.lineEdit.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_2.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_3.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_4.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_5.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_6.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_7.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_8.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_9.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_10.clear()
    ui_super_root_add_community.super_root_add_community.lineEdit_11.clear()
    ui_super_root_add_community.hide()

def switch_window13():  #打开用户查看宠物界面 ，关闭用户界面
    ui_user_pet.show()
    ui_user.hide()
    inquery_user_pet()

def switch_window14():  #打开用户查看员工界面 ，关闭用户界面
    ui_user_staff.show()
    ui_user.hide()
    inquery_user_staff()

def switch_window15():  #打开用户查看车辆界面 ，关闭用户界面
    ui_user_car.show()
    ui_user.hide()
    inquery_user_car_parking()

def switch_window16():  # 打开用户界面，关闭用户查看宠物界面
     ui_user.show()
     ui_user_pet.hide()

def switch_window17():  # 打开用户界面，关闭用户查看员工界面
    ui_user.show()
    ui_user_staff.hide()

def switch_window18():  # 打开用户界面，关闭用户查看车辆界面
    ui_user.show()
    ui_user_car.hide()


def switch_window19():  #  打开小区信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_community.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window20():  #  打开家庭信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_family.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window21():  #  打开员工信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_staff.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window22():  #  打开楼栋信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_build.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window23():  #  打开停车场信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_parking.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window24():  #  打开车辆信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_car.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window25():  #  打开宠物信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_pet.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window26():  #  打开业主信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
    ui_root_house_owner.show()
    if login_data2 == 0:
        ui_super_root_inquery.hide()
    elif login_data2 == 1:
        ui_root.hide()

def switch_window27():  #  关闭小区信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_community.community.tableWidget.clearContents()
    ui_root_community.community.lineEdit.clear()
    ui_root_community.community.lineEdit_2.clear()
    ui_root_community.community.lineEdit_3.clear()
    ui_root_community.community.lineEdit_4.clear()
    ui_root_community.community.lineEdit_5.clear()
    ui_root_community.hide()

def switch_window28():  #  关闭家庭信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_family.family.lineEdit_1.clear()
    ui_root_family.family.lineEdit_2.clear()
    ui_root_family.family.lineEdit_3.clear()
    ui_root_family.family.lineEdit_4.clear()
    ui_root_family.family.lineEdit_5.clear()
    ui_root_family.family.lineEdit_6.clear()
    ui_root_family.family.tableWidget.clearContents()
    ui_root_family.hide()

def switch_window29():  #  关闭员工信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_staff.staff.lineEdit.clear()
    ui_root_staff.staff.lineEdit_2.clear()
    ui_root_staff.staff.lineEdit_3.clear()
    ui_root_staff.staff.lineEdit_4.clear()
    ui_root_staff.staff.lineEdit_5.clear()
    ui_root_staff.staff.lineEdit_6.clear()
    ui_root_staff.staff.lineEdit_7.clear()
    ui_root_staff.staff.lineEdit_8.clear()
    ui_root_staff.staff.tableWidget.clearContents()
    ui_root_staff.hide()

def switch_window30():  #  关闭楼栋信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_build.build.lineEdit.clear()
    ui_root_build.build.lineEdit_2.clear()
    ui_root_build.build.lineEdit_3.clear()
    ui_root_build.build.lineEdit_4.clear()
    ui_root_build.build.lineEdit_5.clear()
    ui_root_build.build.lineEdit_6.clear()
    ui_root_build.build.tableWidget.clearContents()
    ui_root_build.hide()

def switch_window31():  #  关闭停车场信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_parking.parking.lineEdit.clear()
    ui_root_parking.parking.lineEdit_2.clear()
    ui_root_parking.parking.tableWidget.clearContents()
    ui_root_parking.hide()

def switch_window32():  #  关闭车辆信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_car.car.lineEdit.clear()
    ui_root_car.car.lineEdit_2.clear()
    ui_root_car.car.lineEdit_3.clear()
    ui_root_car.car.lineEdit_4.clear()
    ui_root_car.car.lineEdit_5.clear()
    ui_root_car.car.tableWidget.clearContents()
    ui_root_car.hide()

def switch_window33(i):  #  关闭宠物信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_pet.pet.lineEdit.clear()
    ui_root_pet.pet.lineEdit_2.clear()
    ui_root_pet.pet.lineEdit_3.clear()
    ui_root_pet.pet.lineEdit_4.clear()
    ui_root_pet.pet.lineEdit_5.clear()
    ui_root_pet.pet.tableWidget.clearContents()
    ui_root_pet.hide()

def switch_window34():  #  关闭业主信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
    if login_data2 == 0:
        ui_super_root_inquery.show()
    elif login_data2 == 1:
        ui_root.show()
    ui_root_house_owner.house_owner.lineEdit.clear()
    ui_root_house_owner.house_owner.lineEdit_2.clear()
    ui_root_house_owner.house_owner.lineEdit_3.clear()
    ui_root_house_owner.house_owner.lineEdit_4.clear()
    ui_root_house_owner.house_owner.lineEdit_5.clear()
    ui_root_house_owner.house_owner.lineEdit_6.clear()
    ui_root_house_owner.house_owner.tableWidget_2.clearContents()
    ui_root_house_owner.hide()


def test_login():   #检验登入过程
        global login_data1, login_data2, community_id
        text1 = ui_login.login.lineEdit.text()
        text2 = ui_login.login.lineEdit_2.text()
        x, y = connect_mysql.sql_login(text1, text2)
        login_data1 = text1
        login_data2 = y
        print(x, y)
        if x == 2:
            if y == 0:
                switch_window1()   #打开超级管理员界面,关闭登入界面
            if y == 1:
                community_id = connect_mysql.sql_judge_h_e(text1)
                switch_window2()   #打开普通管理员界面，关闭登入界面
            if y == 2:
                community_id = connect_mysql.sql_judge_h_e(text1)
                switch_window3()  #打开业主界面,关闭登入界面
        else:
             QtWidgets.QMessageBox.critical(ui_login, '错误', '用户名或密码错误')

#用户查询

# 业主查询小区信息
def inquery_user_community():
    global login_data1, login_data2
    communicate_data, x = connect_mysql.sql_query_h_e(login_data1, login_data2)
    if not communicate_data:
        communicate_data = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data, x)
    row = x  # 记录行数
    col = len(communicate_data)  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_user.user.tableWidget.setRowCount(row)
    ui_user.user.tableWidget.setColumnCount(col)
    for i in range(row):
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = communicate_data[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_user.user.tableWidget.setItem(i, j, data)

# 业主查询自己信息
def inquery_user_people():
    global login_data1, login_data2
    communicate_data, x= connect_mysql.sql_query_f_people(login_data1)
    if not communicate_data:
        communicate_data = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data, x)
    row = x  # 记录行数
    col = len(communicate_data)  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_user.user.tableWidget_2.setRowCount(row)
    ui_user.user.tableWidget_2.setColumnCount(col)
    for i in range(row):
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = communicate_data[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_user.user.tableWidget_2.setItem(i, j, data)

# 业主查询家庭信息
def inquery_user_family():
    global login_data1, login_data2
    communicate_data, x= connect_mysql.sql_query_f_family(login_data1)
    if not communicate_data:
        communicate_data = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data, x)
    row = x  # 记录行数
    col = len(communicate_data)  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_user.user.tableWidget_3.setRowCount(row)
    ui_user.user.tableWidget_3.setColumnCount(col)
    for i in range(row):
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = communicate_data[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_user.user.tableWidget_3.setItem(i, j, data)

# 业主查询宠物信息
def inquery_user_pet():
    global login_data1, login_data2
    communicate_data, x = connect_mysql.sql_query_f_pet(login_data1)
    if not communicate_data:
        communicate_data = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_user_pet, '宠物信息', '未查询到任何宠物信息')
    else:
        col = len(communicate_data[0])  # 记录列数
        print("行数和列数")
        print(row, col)
        ui_user_pet.user_pet.tableWidget.setRowCount(row)
        ui_user_pet.user_pet.tableWidget.setColumnCount(col)
        for i in range(row):
            text = communicate_data[i]
            for j in range(col):
                # 临时记录，不能直接插入表格
                temp_data = text[j]
                # 转换后可插入表格
                data = QTableWidgetItem(str(temp_data))
                ui_user_pet.user_pet.tableWidget.setItem(i, j, data)

# 业主查询家庭车辆和停车位信息
def inquery_user_car_parking():
    global login_data1, login_data2
    communicate_data1, x1 = connect_mysql.sql_query_f_car(login_data1)  #车辆信息
    if not communicate_data1:
        communicate_data1 = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data1, x1)
    row1 = x1  # 记录行数
    if row1 == 0:
        QMessageBox.information(ui_user_car, '车辆信息', '未查询到任何车辆信息')
    else:
        col1 = len(communicate_data1[0])  # 记录列数
        print("行数和列数")
        print(row1, col1)
        ui_user_car.user_car.tableWidget.setRowCount(row1)
        ui_user_car.user_car.tableWidget.setColumnCount(col1)

        for i in range(row1):
            text = communicate_data1[i]
            for j in range(col1):
                # 临时记录，不能直接插入表格
                temp_data = text[j]
                # 转换后可插入表格
                data = QTableWidgetItem(str(temp_data))
                ui_user_car.user_car.tableWidget.setItem(i, j, data)

    communicate_data2, x2 = connect_mysql.sql_query_f_parking(login_data1)  # 停车位信息
    if not communicate_data2:
        communicate_data2 = ('null', 'null', 'null', 'null', 'null')
    print(communicate_data2, x2)
    row2 = x2  # 记录行数
    if row2 == 0:
        QMessageBox.information(ui_user_car, '停车位信息', '未查询到任何停车位信息')
    else:
        col2 = len(communicate_data2[0])  # 记录列数
        print("行数和列数")
        print(row2, col2)
        ui_user_car.user_car.tableWidget_2.setRowCount(row2)
        ui_user_car.user_car.tableWidget_2.setColumnCount(col2)

        for i in range(row2):
            text = communicate_data2[i]
            for j in range(col2):
                # 临时记录，不能直接插入表格
                temp_data = text[j]
                # 转换后可插入表格
                data = QTableWidgetItem(str(temp_data))
                ui_user_car.user_car.tableWidget_2.setItem(i, j, data)

# 业主查询员工信息
def inquery_user_staff():
    global login_data1, login_data2,community_id
    communicate_data, x = connect_mysql.sql_query_f_staff(community_id)
    print(communicate_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_user_staff, '员工信息', '未查询到任何员工信息')
    else:
        col = len(communicate_data[0])  # 记录列数
        print("行数和列数")
        print(row, col)
        ui_user_staff.user_staff.tableWidget_2.setRowCount(row)
        ui_user_staff.user_staff.tableWidget_2.setColumnCount(col)

        for i in range(row):
            text = communicate_data[i]
            for j in range(col):
                # 临时记录，不能直接插入表格
                temp_data = text[j]
                # 转换后可插入表格
                data = QTableWidgetItem(str(temp_data))
                ui_user_staff.user_staff.tableWidget_2.setItem(i, j, data)


#管理员查询

#普通管理员查询户主信息
def inquery_root_house_owner():
    global community_id
    house_owner_data, x = connect_mysql.sql_query_root_people_owner(community_id)
    print( house_owner_data , x, )
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_house_owner, '住户信息', '未查询到任何住户信息')
    else:
        col = len( house_owner_data[0])  # 记录列数
        print("行数和列数")
        print(row, col)
        ui_root_house_owner.house_owner.tableWidget_2.setRowCount(row)
        ui_root_house_owner.house_owner.tableWidget_2.setColumnCount(col)
        for i in range(row):
            text = house_owner_data[i]
            for j in range(col):
                # 临时记录，不能直接插入表格
                temp_data = text[j]
                # 转换后可插入表格
                data = QTableWidgetItem(str(temp_data))
                ui_root_house_owner.house_owner.tableWidget_2.setItem(i, j, data)

#普通管理员通过少量信息查询户主信息
def inquery_root_house_owner_2():
    global community_id
    f_id = ui_root_house_owner.house_owner.lineEdit.text()
    name = ui_root_house_owner.house_owner.lineEdit_2.text()
    sex = ui_root_house_owner.house_owner.lineEdit_3.text()
    age = ui_root_house_owner.house_owner.lineEdit_4.text()
    id_card = ui_root_house_owner.house_owner.lineEdit_5.text()
    phone_number = ui_root_house_owner.house_owner.lineEdit_6.text()
    data = [f_id, name, sex, age, id_card, phone_number]

    if f_id == '':
        data[0] = -1
    if name == '':
        data[1] = -1
    if sex == '':
        data[2] = -1
    if age == '':
        data[3] = -1
    if id_card == '':
        data[4] = -1
    if phone_number == '':
        data[5] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(6):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 6:
        house_owner_data, x = connect_mysql.sql_query_root_p_search(data1, community_id)
        print( house_owner_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_house_owner, '住户信息', '未查询到任何住户信息')
        else:
            col = len( house_owner_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_house_owner.house_owner.tableWidget_2.setRowCount(row)
            ui_root_house_owner.house_owner.tableWidget_2.setColumnCount(col)
            for i in range(row):
                text = house_owner_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_house_owner.house_owner.tableWidget_2.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_house_owner, '错误', '未填写任何值')

#普通管理员查询楼栋信息
def inquery_root_build():
    global community_id
    community_data, x = connect_mysql.sql_query_root_building(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_build, '楼栋信息', '未查询到任何楼栋信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_build.build.tableWidget.setRowCount(row)
    ui_root_build.build.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_build.build.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询楼栋信息
def inquery_root_build_2():
    global community_id
    text1 = ui_root_build.build.lineEdit.text()
    text2 = ui_root_build.build.lineEdit_2.text()
    text3= ui_root_build.build.lineEdit_3.text()
    text4 = ui_root_build.build.lineEdit_4.text()
    text5 = ui_root_build.build.lineEdit_5.text()
    text6 = ui_root_build.build.lineEdit_6.text()
    data = [text1, text2, text3, text4, text5, text6]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    if text3 == '':
        data[2] = -1
    if text4 == '':
        data[3] = -1
    if text5 == '':
        data[4] = -1
    if text6 == '':
        data[5] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(6):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 6:
        community_data, x = connect_mysql.sql_query_root_b_search(data1,community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_build, '楼栋信息', '未查询到任何楼栋信息')
        else:
            col = len( community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_build.build.tableWidget.setRowCount(row)
            ui_root_build.build.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_build.build.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_build, '错误', '未填写任何值')

#普通管理员查询停车位信息
def inquery_root_parking():
    global community_id
    community_data, x = connect_mysql.sql_query_root_parking(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_parking, '停车位信息', '未查询到任何停车位信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_parking.parking.tableWidget.setRowCount(row)
    ui_root_parking.parking.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_parking.parking.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询停车位信息
def inquery_root_parking_2():
    global community_id
    text1 = ui_root_parking.parking.lineEdit.text()
    text2 = ui_root_parking.parking.lineEdit_2.text()
    data = [text1, text2]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(2):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 2:
        community_data, x = connect_mysql.sql_query_root_parking_search(data1, community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_parking, '停车位信息', '未查询到任何停车位信息')
        else:
            col = len( community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_parking.parking.tableWidget.setRowCount(row)
            ui_root_parking.parking.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_parking.parking.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_build, '错误', '未填写任何值')

#普通管理员查询车辆信息
def inquery_root_car():
    global community_id
    community_data, x = connect_mysql.sql_query_root_car(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_car, '停车位信息', '未查询到任何停车位信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_car.car.tableWidget.setRowCount(row)
    ui_root_car.car.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_car.car.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询车辆信息
def inquery_root_car_2():
    global community_id
    text1 = ui_root_car.car.lineEdit.text()
    text2 = ui_root_car.car.lineEdit_2.text()
    text3= ui_root_car.car.lineEdit_3.text()
    text4 = ui_root_car.car.lineEdit_4.text()
    text5 = ui_root_car.car.lineEdit_5.text()
    data = [text1, text2, text3, text4, text5]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    if text3 == '':
        data[2] = -1
    if text4 == '':
        data[3] = -1
    if text5 == '':
        data[4] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(5):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 5:
        community_data, x = connect_mysql.sql_query_root_car_search(data1, community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_car, '车辆信息', '未查询到任何车辆信息')
        else:
            col = len( community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_car.car.tableWidget.setRowCount(row)
            ui_root_car.car.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_car.car.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_car, '错误', '未填写任何值')

#普通管理员查询宠物信息
def inquery_root_pet():
    global community_id
    community_data, x = connect_mysql.sql_query_root_pet(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_pet, '宠物信息', '未查询到任何宠物信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_pet.pet.tableWidget.setRowCount(row)
    ui_root_pet.pet.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_pet.pet.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询宠物信息
def inquery_root_pet_2():
    global community_id
    text1 = ui_root_pet.pet.lineEdit.text()
    text2 = ui_root_pet.pet.lineEdit_2.text()
    text3 = ui_root_pet.pet.lineEdit_3.text()
    text4 = ui_root_pet.pet.lineEdit_4.text()
    text5 = ui_root_pet.pet.lineEdit_5.text()
    data = [text1, text2, text3, text4, text5]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    if text3 == '':
        data[2] = -1
    if text4 == '':
        data[3] = -1
    if text5 == '':
        data[4] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(5):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 5:
        community_data, x = connect_mysql.sql_query_root_pet_search(data1, community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_pet, '宠物信息', '未查询到任何宠物信息')
        else:
            col = len( community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_pet.pet.tableWidget.setRowCount(row)
            ui_root_pet.pet.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_pet.pet.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_pet, '错误', '未填写任何值')

#普通管理员查询员工信息
def inquery_root_staff():
    global community_id
    community_data, x = connect_mysql.sql_query_root_staff(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_staff, '员工信息', '未查询到任何员工信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_staff.staff.tableWidget.setRowCount(row)
    ui_root_staff.staff.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_staff.staff.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询员工信息
def inquery_root_staff_2():
    global community_id
    text1 = ui_root_staff.staff.lineEdit.text()
    text2 = ui_root_staff.staff.lineEdit_2.text()
    text3 = ui_root_staff.staff.lineEdit_3.text()
    text4 = ui_root_staff.staff.lineEdit_4.text()
    text5 = ui_root_staff.staff.lineEdit_5.text()
    text6 = ui_root_staff.staff.lineEdit_6.text()
    text7 = ui_root_staff.staff.lineEdit_7.text()
    text8 = ui_root_staff.staff.lineEdit_8.text()
    data = [text1, text2, text3, text4, text5, text6, text7, text8]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    if text3 == '':
        data[2] = -1
    if text4 == '':
        data[3] = -1
    if text5 == '':
        data[4] = -1
    if text6 == '':
        data[5] = -1
    if text7 == '':
        data[6] = -1
    if text8 == '':
        data[7] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(8):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 8:
        community_data, x = connect_mysql.sql_query_root_staff_search(data1, community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_staff, '员工信息', '未查询到任何员工信息')
        else:
            col = len( community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_staff.staff.tableWidget.setRowCount(row)
            ui_root_staff.staff.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_staff.staff.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_staff, '错误', '未填写任何值')

#普通管理员查询家庭信息
def inquery_root_family():
    global community_id
    community_data, x = connect_mysql.sql_query_root_family(community_id)
    print(community_data, x)
    row = x  # 记录行数
    if row == 0:
        QMessageBox.information(ui_root_family, '家庭信息', '未查询到任何家庭信息')
    col = len( community_data[0])  # 记录列数
    print("行数和列数")
    print(row, col)
    ui_root_family.family.tableWidget.setRowCount(row)
    ui_root_family.family.tableWidget.setColumnCount(col)
    for i in range(row):
        text = community_data[i]
        for j in range(col):
            # 临时记录，不能直接插入表格
            temp_data = text[j]
            # 转换后可插入表格
            data = QTableWidgetItem(str(temp_data))
            ui_root_family.family.tableWidget.setItem(i, j, data)

#普通管理员通过少量信息查询家庭信息
def inquery_root_family_2():
    global community_id
    text1 = ui_root_family.family.lineEdit_1.text()
    text2 = ui_root_family.family.lineEdit_2.text()
    text3 = ui_root_family.family.lineEdit_3.text()
    text4 = ui_root_family.family.lineEdit_4.text()
    text5 = ui_root_family.family.lineEdit_5.text()
    text6 = ui_root_family.family.lineEdit_6.text()
    data = [text1, text2, text3, text4, text5, text6]
    print(data)
    if text1 == '':
        data[0] = -1
    if text2 == '':
        data[1] = -1
    if text3 == '':
        data[2] = -1
    if text4 == '':
        data[3] = -1
    if text5 == '':
        data[4] = -1
    if text6 == '':
        data[5] = -1
    data1 = tuple(data)
    print(data1)
    flag = 0
    for index in range(6):
        if data1[index] == -1:
            flag += 1
    print(flag)
    if flag != 6:
        community_data, x = connect_mysql.sql_query_root_family_search(data1, community_id)
        print(community_data, x)
        row = x  # 记录行数
        if row == 0:
            QMessageBox.information(ui_root_family, '家庭信息', '未查询到任何家庭信息')
        else:
            col = len(community_data[0])  # 记录列数
            print("行数和列数")
            print(row, col)
            ui_root_family.family.tableWidget.setRowCount(row)
            ui_root_family.family.tableWidget.setColumnCount(col)
            for i in range(row):
                text = community_data[i]
                for j in range(col):
                    # 临时记录，不能直接插入表格
                    temp_data = text[j]
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(temp_data))
                    ui_root_family.family.tableWidget.setItem(i, j, data)
    else:
        QMessageBox.critical(ui_root_family, '错误', '未填写任何值')

#继承login类
class login_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.login = Ui_login()
        self.login.setupUi(self)


        self.login.pushButton.clicked.connect(test_login) # 敲击登入按钮
        self.login.pushButton_2.clicked.connect(switch_window4) #点击修改密码按钮
        self.login.pushButton_3.clicked.connect(exit)  #敲击退出系统按钮

# 继承Ui_change_password类
class change_password_Window(QDialog):
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

        self.change_password.pushButton.clicked.connect(test_change_password)  # 显示确认是否修改密码弹窗
        self.change_password.pushButton_2.clicked.connect(switch_window5)#从修改界面返回登入界面

# 继承Ui_super_root类
class super_root_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.super_root = Ui_super_root()
        self.super_root.setupUi(self)
        def access_delete():
            text = ui_super_root.super_root.lineEdit.text()


        self.super_root.pushButton.clicked.connect(switch_window10) #进入小区查询界面
       # self.super_root.pushButton_3.clicked.connect()   #删除小区

        self.super_root.pushButton_2.clicked.connect(switch_window9) # 打开添加小区界面，关闭超级管理员界面
        self.super_root.pushButton_4.clicked.connect(switch_window8) #打开登入界面，关闭超级管理员界面
        self.super_root.pushButton_5.clicked.connect(exit)

# 继承Ui_super_root_inquery类
class super_root_inquery_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.super_root_inquery = Ui_super_root_inquery()
        self.super_root_inquery.setupUi(self)

        self.super_root_inquery.pushButton.clicked.connect(switch_window19)   #  打开小区信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_2.clicked.connect(switch_window20) #  打开家庭信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_3.clicked.connect(switch_window21) #  打开员工信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_4.clicked.connect(switch_window22) #  打开楼栋信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_5.clicked.connect(switch_window23) #  打开停车场信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_6.clicked.connect(switch_window24) #  打开车辆信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_7.clicked.connect(switch_window25) #  打开宠物信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.super_root_inquery.pushButton_8.clicked.connect(switch_window26) #  打开业主信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面

        self.super_root_inquery.pushButton_9.clicked.connect(switch_window11)  # 打开超级管理员界面，关闭小区查询界面
        self.super_root_inquery.pushButton_10.clicked.connect(exit)

# 继承Ui_super_root_add_community类
class super_root_add_community_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.super_root_add_community = Ui_super_root_add_community()
        self.super_root_add_community.setupUi(self)
        self.super_root_add_community.pushButton_4.clicked.connect(switch_window12)   #打开超级管理员界面 ，关闭添加小区界面
        self.super_root_add_community.pushButton_6.clicked.connect(exit)

# 继承Ui_root类
class root_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.root = Ui_root()
        self.root.setupUi(self)
        self.root.pushButton.clicked.connect(switch_window19)   #  打开小区信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_2.clicked.connect(switch_window20) #  打开家庭信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_3.clicked.connect(switch_window21) #  打开员工信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_4.clicked.connect(switch_window22) #  打开楼栋信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_5.clicked.connect(switch_window23) #  打开停车场信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_6.clicked.connect(switch_window24) #  打开车辆信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_7.clicked.connect(switch_window25) #  打开宠物信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_8.clicked.connect(switch_window26) #  打开业主信息界面，0表示关闭超级管理员界面，1表示关闭普通管理员界面
        self.root.pushButton_9.clicked.connect(switch_window7)  # 打开登入界面，关闭管理员界面
        self.root.pushButton_10.clicked.connect(exit)

#继承root_community类
class root_community_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.community = Ui_root_community()
        self.community.setupUi(self)
        def shuaxin(): #刷新页面
            self.community.tableWidget.clearContents()
            self.community.lineEdit.clear()
            self.community.lineEdit_2.clear()
            self.community.lineEdit_3.clear()
            self.community.lineEdit_4.clear()
            self.community.lineEdit_5.clear()
            ui_root_community.hide()
            ui_root_community.show()

        self.community.pushButton_1.clicked.connect(shuaxin)
        self.community.pushButton_4.clicked.connect(switch_window27) #  关闭小区信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.community.pushButton_6.clicked.connect(exit)

#继承root_family类
class root_family_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.family = Ui_root_family()
        self.family.setupUi(self)
        def shuaxin(): #刷新页面
            self.family.tableWidget.clearContents()
            self.family.lineEdit_1.clear()
            self.family.lineEdit_2.clear()
            self.family.lineEdit_3.clear()
            self.family.lineEdit_4.clear()
            self.family.lineEdit_5.clear()
            self.family.lineEdit_6.clear()
            ui_root_family.hide()
            ui_root_family.show()

        self.family.pushButton_1.clicked.connect(inquery_root_family) #全部查询
        self.family.pushButton_2.clicked.connect(shuaxin)
        self.family.pushButton_3.clicked.connect(inquery_root_family_2) #少量信息查询
        self.family.pushButton_7.clicked.connect(switch_window28)   #  关闭家庭信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.family.pushButton_21.clicked.connect(exit)

#继承root_staff类
class root_staff_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.staff = Ui_root_staff()
        self.staff.setupUi(self)
        def shuaxin(): #刷新页面
            self.staff.tableWidget.clearContents()
            self.staff.lineEdit.clear()
            self.staff.lineEdit_2.clear()
            self.staff.lineEdit_3.clear()
            self.staff.lineEdit_4.clear()
            self.staff.lineEdit_5.clear()
            self.staff.lineEdit_6.clear()
            self.staff.lineEdit_7.clear()
            self.staff.lineEdit_8.clear()
            ui_root_staff.hide()
            ui_root_staff.show()

        self.staff.pushButton.clicked.connect(inquery_root_staff) #全部查询
        self.staff.pushButton_1.clicked.connect(shuaxin)
        self.staff.pushButton_2.clicked.connect(inquery_root_staff_2) #通过少量信息查询员工信息
        self.staff.pushButton_6.clicked.connect(switch_window29)  #  关闭员工信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.staff.pushButton_7.clicked.connect(exit)

#继承root_build类
class root_build_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.build = Ui_root_build()
        self.build.setupUi(self)
        def shuaxin(): #刷新页面
            self.build.tableWidget.clearContents()
            self.build.lineEdit.clear()
            self.build.lineEdit_2.clear()
            self.build.lineEdit_3.clear()
            self.build.lineEdit_4.clear()
            self.build.lineEdit_5.clear()
            self.build.lineEdit_6.clear()
            ui_root_build.hide()
            ui_root_build.show()

        self.build.pushButton_1.clicked.connect(shuaxin)
        self.build.pushButton.clicked.connect(inquery_root_build)   #普通管理员查询楼栋信息
        self.build.pushButton_2.clicked.connect(inquery_root_build_2)  #普通管理员通过少量信息查询楼栋信息
        self.build.pushButton_6.clicked.connect(switch_window30)   #  关闭楼栋信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.build.pushButton_7.clicked.connect(exit)

#继承root_parking类
class root_parking_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.parking = Ui_root_parking()
        self.parking.setupUi(self)
        def shuaxin(): #刷新页面
            self.parking.tableWidget.clearContents()
            self.parking.lineEdit.clear()
            self.parking.lineEdit_2.clear()
            ui_root_parking.hide()
            ui_root_parking.show()

        self.parking.pushButton.clicked.connect(inquery_root_parking) #全部查询
        self.parking.pushButton_2.clicked.connect(shuaxin)
        self.parking.pushButton_3.clicked.connect(inquery_root_parking_2) #通过少量信息查询停车场信息
        self.parking.pushButton_7.clicked.connect(switch_window31)  #  关闭停车场信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.parking.pushButton_8.clicked.connect(exit)

#继承root_car类
class root_car_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.car = Ui_root_car()
        self.car.setupUi(self)
        def shuaxin(): #刷新页面
            self.car.tableWidget.clearContents()
            self.car.lineEdit.clear()
            self.car.lineEdit_2.clear()
            self.car.lineEdit_3.clear()
            self.car.lineEdit_4.clear()
            self.car.lineEdit_5.clear()
            ui_root_car.hide()
            ui_root_car.show()

        self.car.pushButton.clicked.connect(inquery_root_car) #全部查询
        self.car.pushButton_2.clicked.connect(shuaxin)
        self.car.pushButton_3.clicked.connect(inquery_root_car_2) #通过少量信息查询车辆信息
        self.car.pushButton_7.clicked.connect(switch_window32)  #  关闭车辆信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.car.pushButton_8.clicked.connect(exit)

#继承root_pet类
class root_pet_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.pet = Ui_root_pet()
        self.pet.setupUi(self)
        def shuaxin(): #刷新页面
            self.pet.tableWidget.clearContents()
            self.pet.lineEdit.clear()
            self.pet.lineEdit_2.clear()
            self.pet.lineEdit_3.clear()
            self.pet.lineEdit_4.clear()
            self.pet.lineEdit_5.clear()
            ui_root_pet.hide()
            ui_root_pet.show()

        self.pet.pushButton.clicked.connect(inquery_root_pet) #全部查询
        self.pet.pushButton_2.clicked.connect(shuaxin)
        self.pet.pushButton_3.clicked.connect(inquery_root_pet_2) #通过部分信息插查询宠物信息
        self.pet.pushButton_7.clicked.connect(switch_window33) #  关闭宠物信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.pet.pushButton_9.clicked.connect(exit)

#继承root_house_owner类
class root_house_owner_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.house_owner = Ui_root_house_owner()
        self.house_owner.setupUi(self)
        def shuaxin(): #刷新页面
            self.house_owner.tableWidget_2.clearContents()
            self.house_owner.lineEdit.clear()
            self.house_owner.lineEdit_2.clear()
            self.house_owner.lineEdit_3.clear()
            self.house_owner.lineEdit_4.clear()
            self.house_owner.lineEdit_5.clear()
            self.house_owner.lineEdit_6.clear()
            ui_root_house_owner.hide()
            ui_root_house_owner.show()

        self.house_owner.pushButton.clicked.connect(inquery_root_house_owner)  #普通管理员查询户主信息
        self.house_owner.pushButton_2.clicked.connect(shuaxin)
        self.house_owner.pushButton_3.clicked.connect(inquery_root_house_owner_2)  #普通管理员通过少量信息查询户主信息
        self.house_owner.pushButton_7.clicked.connect(switch_window34)  # 关闭业主信息界面，0表示打开超级管理员界面，1表示打开普通管理员界面
        self.house_owner.pushButton_14.clicked.connect(exit)

# 继承Ui_user类
class user_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.user = Ui_user()
        self.user.setupUi(self)
        self.user.pushButton.clicked.connect(switch_window13) #打开用户查看宠物界面 ，关闭用户界面
        self.user.pushButton_2.clicked.connect(switch_window14) #打开用户查看员工界面 ，关闭用户界面
        self.user.pushButton_3.clicked.connect(switch_window15) #打开用户查看车辆界面 ，关闭用户界面
        self.user.pushButton_5.clicked.connect(switch_window6)#打开登入界面，关闭用户界面
        self.user.pushButton_6.clicked.connect(exit)

# 继承Ui_user_car类
class user_pet_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.user_pet= Ui_user_pet()
        self.user_pet.setupUi(self)
        self.user_pet.pushButton.clicked.connect(switch_window16) # 打开用户界面，关闭用户查看宠物界面

# 继承Ui_user_car类
class user_staff_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.user_staff= Ui_user_staff()
        self.user_staff.setupUi(self)
        self.user_staff.pushButton.clicked.connect(switch_window17)  # 打开用户界面，关闭用户查看员工界面

# 继承Ui_user_car类
class user_car_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.user_car = Ui_user_car()
        self.user_car.setupUi(self)
        self.user_car.pushButton.clicked.connect(switch_window18)  #打开用户界面，关闭用户查看车辆界面


app = QtWidgets.QApplication(sys.argv)
ui_login = login_window()
ui_change_password = change_password_Window()

ui_super_root = super_root_Window()
ui_super_root_inquery = super_root_inquery_Window()
ui_super_root_add_community = super_root_add_community_Window()


ui_root = root_Window()
ui_root_build = root_build_window()
ui_root_car = root_car_window()
ui_root_community = root_community_window()
ui_root_family = root_family_window()
ui_root_house_owner = root_house_owner_window()
ui_root_parking = root_parking_window()
ui_root_pet = root_pet_window()
ui_root_staff = root_staff_window()


ui_user = user_Window()
ui_user_car = user_car_Window()
ui_user_pet = user_pet_Window()
ui_user_staff = user_staff_Window()

# z = ['f001001', '', '', '', '', '']
#
# if z[3]=='':
#     z[3]= -1
# if z[2] =='':
#     z[2] = -1
# if z[1] == '':
#     z[1] =-1
# if z[4] =='':
#     z[4]=-1
# if z[5] == '':
#     z[5]=-1
# d = tuple(z)
# print(d)
# x, y =connect_mysql.sql_query_root_p_search(d, '001')
# print(x)

ui_login.show()
sys.exit(app.exec_())

conn.close()



