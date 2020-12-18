import pymysql
from PyQt5 import *
import sys
from PyQt5.QtWidgets import *
from login import *

#链接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='ssh_crud',
    charset='utf8')
cursor = conn.cursor()

#登陆
def sql_login(a, b):
    #定义变量
    value1 = (a,)
    value2 = (b,)
    table = ['admin','family_account_number','staff_account_number']
    flag = 0
    sql1 = "select id from admin"
    sql2 = "select id from family_account_number"
    sql3 = "select id from staff_account_number"

    #从数据库中查询信息
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()

    #判断登陆的用户的用户类型
    #超级管理员
    for myret1 in ret1:
        if value1 == myret1:
            flag = 1
            user = 0
            break
    #用户
    if flag == 0:
        for myret2 in ret2:
            if value1 == myret2:
                flag = 2
                user = 2
                break
    #普通管理员
    if flag == 0:
        for myret3 in ret3:
            if value1 == myret3:
                flag = 3
                user = 1
                break

    #查询并获取密码
    sql4 = "select password from " + table[flag-1] + " where(id = \'" + a + "\');"
    cursor.execute(sql4)
    ret = cursor.fetchone()

    #判断是否登陆成功
    conn.commit()
    if flag == 0:
        return 0#用户名不存在
    if value2 == ret:
        return 2,user#登陆成功，user为整型值，0，1，2对应超级管理员，普通管理员，用户
    else:
        return 1#密码错误


#修改密码
def sql_change_password(a, b, c, d):
    #定义变量
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

    #从数据库读取数据
    cursor.execute(sql1)
    ret1 = cursor.fetchall()
    cursor.execute(sql2)
    ret2 = cursor.fetchall()
    cursor.execute(sql3)
    ret3 = cursor.fetchall()

    #判断尝试登陆的是哪个用户
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

    #寻找密码的mysql语句
    sql4 = "select password from " + table[table_number-1] + " where(id = \'" + a + "\');"

    #从数据库中寻找密码
    cursor.execute(sql4)
    ret = cursor.fetchone()

    #修改密码语句
    sql5 = "update " + table[table_number - 1] + " set password = \'" + c + "\' where id = \'" + a + "\';"

    #根据不同状态返回值
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

#查询小区信息
def sql_query_h_e(a,b):
    #定义变量
    value1 = (a,)
    value2 = (b,)

    #查询用户所在小区
    query_id0 = "select h_e_id from staff,staff_account_number where " \
                "staff.id = staff_account_number.staff_id " \
                "and staff.id = \'" + a + "\';"
    query_id1 = "select h_e_id from family,family_account_number where " \
                "family.id = family_account_number.f_id " \
                "and family.id = \'" + a + "\';"
    if b == 1:
        cursor.execute(query_id0)
        h_e_id = cursor.fetchone()
    elif b == 2:
        cursor.execute(query_id1)
        h_e_id = cursor.fetchone()

    #定义sql查询语句
    sql0 = "select * from housing_estate;"
    sql1 = "select * from housing_estate where id = \'" + h_e_id[0] + "\';"
    sql2 = "select " \
           "h_e_name,h_e_adress,h_e_area,h_e_developer,h_e_staff,h_e_building,h_e_parking " \
           "from housing_estate where id = \'" + h_e_id[0] + "\';"

    #超级管理员
    if b == 0 :
        cursor.execute(sql0)
        ret = cursor.fetchone()
    #普通管理员
    elif b == 1:
        cursor.execute(sql1)
        ret = cursor.fetchone()
    #用户
    elif b == 2:
        cursor.execute(sql2)
        ret = cursor.fetchone()

    return ret

