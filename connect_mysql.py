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
    table = ['admin', 'family_account_number', 'staff_account_number']
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
        return 0, -1#用户名不存在
    if value2 == ret:
        return 2, user#登陆成功，user为整型值，0，1，2对应超级管理员，普通管理员，用户
    else:
        return 1, -1#密码错误


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

#判断用户与普通管理员所在的小区
def sql_judge_h_e(a):#参数a为用户名
    # 查询用户所在小区,h_e_id为小区编号
    query_id0 = "select staff.h_e_id from staff,staff_account_number where " \
                "staff.id = staff_account_number.staff_id " \
                "and staff_account_number.staff_id = \'" + a + "\';"
    query_id1 = "select family.h_e_id from family,family_account_number where " \
                "family.id = family_account_number.f_id " \
                "and family_account_number.f_id = \'" + a + "\';"
    if a[0] == 's':
        cursor.execute(query_id0)
        h_e_id = cursor.fetchone()
    elif a[0] == 'f':
        cursor.execute(query_id1)
        h_e_id = cursor.fetchone()
    return h_e_id[0]

#查询小区信息
def sql_query_h_e(a, b):# a = 用户名 , b = 返回的身份。0，1，2对应超级管理员，普通管理员，用户
    #查询用户所在小区,h_e_id为小区编号
    query_id0 = "select staff.h_e_id from staff,staff_account_number where " \
                "staff.id = staff_account_number.staff_id " \
                "and staff_account_number.staff_id = \'" + a + "\';"
    query_id1 = "select family.h_e_id from family,family_account_number where " \
                "family.id = family_account_number.f_id " \
                "and family_account_number.f_id = \'" + a + "\';"

    if b == 0:
        h_e_id = ('0',)
    elif b == 1:
        cursor.execute(query_id0)
        h_e_id = cursor.fetchone()
    elif b == 2:
        cursor.execute(query_id1)
        h_e_id = cursor.fetchone()
    else:
        return -1, -1
    #定义sql查询语句

    sql0 = "select id,h_e_name,h_e_developer,h_e_area,h_e_staff,h_e_adress,h_e_family,h_e_parking,h_e_pet,h_e_building,h_e_car" \
           "from housing_estate;"
    sql1 = "select id,h_e_name,h_e_developer,h_e_area,h_e_staff,h_e_adress,h_e_family,h_e_parking,h_e_pet,h_e_building,h_e_car" \
           "from housing_estate where id = \'" + h_e_id[0] + "\';"
    sql2 = "select " \
           "h_e_name,h_e_adress,h_e_area,h_e_developer,h_e_staff,h_e_parking " \
           "from housing_estate where id = \'" + h_e_id[0] + "\';"

    #超级管理员
    if b == 0:
        cursor.execute(sql0)
        row = cursor.execute(sql0)
        ret = cursor.fetchall()
    #普通管理员
    elif b == 1:
        cursor.execute(sql1)
        row = cursor.execute(sql1)
        ret = cursor.fetchone()
    #用户
    elif b == 2:
        cursor.execute(sql2)
        row = cursor.execute(sql2)
        ret = cursor.fetchone()
    conn.commit()
    return ret, row
#用户查看自己的户主信息
def sql_query_f_people(a):#参数a为用户名
    sql = "select pname,psex,page,pphone,id from people where f_id = \'" + a + "\';"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchone()
    return ret, row
#用户查看自己的家庭信息
def sql_query_f_family(a):#参数a为用户名
    sql = "select id,family_number,car,parking,pet from family where id = \'" + a + "\';"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchone()
    return ret, row
#用户查看自己的宠物信息
def sql_query_f_pet(a):#参数a用户名
    #定义数据库查询语句
    sql = "select f_id,pet.id,variety,sex,age from pet,family where pet.f_id = family.id and family.id = \'" + a + "\';"
    cursor.execute(sql)
    ret = cursor.fetchall()
    row = cursor.execute(sql)
    conn.commit()
    #返回元组ret(若用户没有宠物则返回空元组)
    return ret, row
#用户查询车辆信息
def sql_query_f_car(a):#参数a用户名
    #定义数据库查询语句
    sql = "select id,color,brand,model from car,family where car.f_id = family.id and family.id = \'" + a + "\';"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row#返回元组ret(若用户没有车辆则返回空元组)
#用户查看自己的小区车位信息
def sql_query_f_parking(a):#参数a为用户名
    #定义数据库语句
    sql = "select housing_estate.h_e_adress,parking.adress from parking,housing_estate,family" \
          " where( housing_estate.id = (select family.h_e_id where family.id = \'" + a + "\') and parking.f_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    return ret, row#返回元组ret(若用户没有车辆则返回空元组)
#用户查看自己小区的员工信息
def sql_query_f_staff(a):#参数a为小区id
    sql = "select staff.id,s_name,staff_position,s_sex,s_age,wages,idcard,telephone " \
          "from staff,housing_estate " \
          "where( staff.h_e_id = housing_estate.id and staff.h_e_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row


#管理员查看当前小区所有户主信息
def sql_query_root_people_owner(a):#参数a为小区id
    sql = "select people.f_id,people.pname,people.psex,people.page,people.id,people.pphone " \
          "from people,family where people.f_id = family.id and  family.h_e_id = \'" + a + "\';"
    print(sql)
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret ,row
#管理员根据检索值查看户主信息
def sql_query_root_p_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select f_id,pname,psex,page,people.id,pphone from " \
          "people,family where(people.f_id = family.id and family.h_e_id = \'" + b + "\' and "
    column = ("people.f_id","people.pname","people.psex","people.page","people.id","people.pphone")
    for i in a :
        if i != -1:
            if a.index(i) != 3 :
                x = a.index(i)
                sql = sql + column[x] + " = \'" + i + "\' and "
            elif a.index(i) == 3:
                x = a.index(i)
                sql = sql + column[x] + " = " + str(i) + " and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret ,row

#管理员查看当前小区所有楼栋信息
def sql_query_root_building(a):#参数a为小区id
    sql = "select building.id,building.b_adress,building.b_family,building.unit,building.floor,building.room " \
           "from building,housing_estate where housing_estate.id = \'" + a + "\';"

    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row
#管理员根据检索值查看当前小区的楼栋信息
def sql_query_root_b_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select building.id,b_adress,b_family,unit,floor,room " \
          "from building,housing_estate where(building.h_e_id = housing_estate.id " \
          "and housing_estate.id = \'" + b + "\' and "
    column = ("building.id", "building.b_adress", "building.b_family", "building.unit", "building.floor", "building.room")
    for i in a:
        if i != -1:
            if a.index(i) == 0 or a.index(i) == 1 :
                x = a.index(i)
                sql = sql + column[x] + " = \'" + i + "\' and "
            else :
                x = a.index(i)
                sql = sql + column[x] + " = " + str(i) + " and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row

#管理员查看当前小区停车位信息
def sql_query_root_parking(a):#参数a为小区编号
    sql = "select f_id,adress from parking where h_e_id = \'" + a + "\';"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row
#管理员根据检索值查看当前小区停车位信息
def sql_query_root_parking_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select f_id,adress from parking where( h_e_id = \'" + b + "\' and "
    column = ("f_id", "adress")
    for i in a:
        if i != -1:
            x = a.index(i)
            sql = sql + column[x] + " = \'" + i + "\' and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret,row

#管理员查看当前小区车辆信息
def sql_query_root_car(a):#参数a为小区id
    sql = "select car.id,f_id,color,brand,model from car,family " \
          "where( car.f_id = family.id and family.h_e_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row
#管理员根据检索值查看当前小区车辆信息
def sql_query_root_car_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select car.id,f_id,color,brand,model from car,family " \
          "where( car.f_id = family.id and family.h_e_id = \'" + b + "\' and "
    column = ("car.id", "f_id","color","brand","model")
    for i in a :
        if i != -1:
            x = a.index(i)
            sql = sql + column[x] + " = \'" + i + "\' and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row

#管理员查看当前小区所有的宠物信息
def sql_query_root_pet(a):#参数a为小区id
    sql = "select f_id,pet.id,variety,sex,age from pet,family " \
          "where( pet.f_id = family.id and family.h_e_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row
#管理员根据检索值查看当前小区的宠物信息
def sql_query_root_pet_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select f_id,pet.id,variety,sex,age from pet,family " \
          "where( pet.f_id = family.id and family.h_e_id = \'" + b + "\' and "
    column = ("f_id", "pet.id", "variety", "sex", "age")
    for i in a :
        if i != -1:
            if a.index(i) != 4:
                x = a.index(i)
                sql = sql + column[x] + " = \'" + i + "\' and "
            else :
                x = a.index(i)
                sql = sql + column[x] + " = " + str(i) + " and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row

#管理员查看当前小区的所有员工信息
def sql_query_root_staff(a):#参数a为小区id
    sql = "select staff.id,s_name,staff_position,s_sex,s_age,wages,idcard,telephone " \
          "from staff,housing_estate " \
          "where( staff.h_e_id = housing_estate.id and staff.h_e_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row
#管理员根据检索值查看当前小区的员工信息
def sql_query_root_staff_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select staff.id,s_name,staff_position,s_sex,s_age,wages,idcard,telephone " \
          "from staff,housing_estate " \
          "where( staff.h_e_id = housing_estate.id and staff.h_e_id = \'" + b + "\' and "
    column = ("staff.id", "s_name", "staff_position", "s_sex", "s_age","wages","idcard","telephone")
    for i in a :
        if i != -1:
            if a.index(i) == 4 or a.index(i) == 5:
                x = a.index(i)
                sql = sql + column[x] + " = " + str(i) + " and "
            else :
                x = a.index(i)
                sql = sql + column[x] + " = \'" + i + "\' and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row

#管理员查看当前小区的所有家庭信息
def sql_query_root_family(a):#参数a为小区id
    sql = "select family.id,family_number,car,parking,people,pet " \
          "from family,housing_estate " \
          "where(family.h_e_id = housing_estate.id and family.h_e_id = \'" + a + "\');"
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret,row

#管理员根据检索值查看当前小区的家庭信息
def sql_query_root_family_search(a,b):#参数a为用户输入的索引值，参数b为小区id
    sql = "select family.id,family_number,car,parking,people,pet " \
          "from family,housing_estate " \
          "where(family.h_e_id = housing_estate.id and family.h_e_id = \'" + b + "\' and "
    column = ("family.id", "family_number", "car", "parking", "people", "pet")
    for i in a :
        if i != -1:
            if a.index(i) == 0 or a.index(i) == 1:
                x = a.index(i)
                sql = sql + column[x] + " = \'" + i + "\' and "
            else :
                x = a.index(i)
                sql = sql + column[x] + " = " + str(i) + " and "
    sql = sql[:-5]
    sql = sql + ' );'
    cursor.execute(sql)
    row = cursor.execute(sql)
    ret = cursor.fetchall()
    conn.commit()
    return ret, row