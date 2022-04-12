# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     python_execute_mysql
   Description :
   Author :       Kirk
   date：          2022/4/12
-------------------------------------------------
   Change Activity:
                   2022/4/12:
-------------------------------------------------
"""
import pymysql

"""# 范例
# 打开数据库连接,当使用本机的数据库时，host='localhost'
db = pymysql.connect(host='192.168.xx.xx', user='root', password='xxxx', database='xxx')

# 使用cursor() 创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")	# 要执行的sql语句

# 使用fetchone()方法获取单条数据.
data = cursor.fetchone()
print("Database Version : {}".format(data))

# 关闭数据库连接
db.close()

"""


# 范例1
def select_sql_version():
    # 打开数据库连接,当使用本机的数据库时，host='localhost'
    db = pymysql.connect(host='localhost', user='root', password='123456', database='tmp')

    # 使用cursor() 创建一个游标对象cursor
    cursor = db.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute("SELECT VERSION()")  # 要执行的sql语句

    # 使用fetchone()方法获取单条数据.
    data = cursor.fetchone()
    print("Database Version : {}".format(data))

    # 关闭数据库连接
    db.close()


# 范例2
def select_sql_version2():
    # 建立数据库连接
    with pymysql.connect(host='localhost', user='root', password='123456', database='tmp') as db:
        # 使用cursor() 创建一个游标对象cursor
        cursor = db.cursor()

        # 使用execute()方法执行SQL查询
        cursor.execute("SELECT VERSION()")  # 要执行的sql语句

        # 使用fetchone()方法获取单条数据.
        data = cursor.fetchone()
        print("Database Version : {}".format(data))


# 范例3
def create_table():
    with pymysql.connect(host='localhost', user='root', password='123456', database='demo') as db:
        # 使用cursor() 创建一个游标对象cursor
        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS my_table")  # 使用excute() 方法执行SQL：如果表存在则删除
        # 使用预处理语句创建表
        sql = """CREATE TABLE my_table(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT)"""
        cursor.execute(sql)  # 通过预处理语句创建表
        # cursor.execute("DROP TABLE IF EXISTS my_table")


# 范例4
def insert_data():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='demo')
    cursor = db.cursor()
    first_name, last_name, age = "Mac", "Mohan", 20
    # sql语句的语法潜规则规定必须有引号将值包起来
    sql = f"""INSERT INTO my_table(FIRST_NAME, LAST_NAME, AGE) VALUES ({repr(first_name)}, {repr(last_name)}, {repr(
        age)})
    """  # repr()函数，可以将转换的字符串带有引号
    try:
        cursor.execute(sql)
        db.commit()  # 增删改数据需要提交事务
        print('插入数据成功')
    except pymysql.err.ProgrammingError:
        db.rollback()
        print("插入数据失败，回滚")
    db.close()


# 范例5
def delete_data():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='demo')
    cursor = db.cursor()
    # sql语句的语法潜规则规定必须有引号将值包起来
    sql = f"""DELETE FROM my_table WHERE AGE = 20;
        """  # repr()函数，可以将转换的字符串带有引号
    try:
        cursor.execute(sql)
        db.commit()  # 增删改数据需要提交事务
        print('删除数据成功')
    except pymysql.err.ProgrammingError:
        db.rollback()
        print("删除数据失败，回滚")
    db.close()


# 范例6
def update_data():
    with pymysql.connect(host='localhost', user='root', password='123456', database='demo') as db:
        cursor = db.cursor()
        sql = """UPDATE my_table SET FIRST_NAME = '%s' WHERE AGE = 20""" % 'Bob'
        try:
            cursor.execute(sql)
            db.commit()  # 更新数据需要提交事务
            print('更新数据成功')
        except pymysql.err.ProgrammingError:
            db.rollback()
            print("更新数据失败，回滚")


# 范例7
def select_data():
    with pymysql.connect(host='localhost', user='root', password='123456', database='tmp') as db:
        cursor = db.cursor()
        sql = "SELECT * FROM emp WHERE sal > %d" % 2000
        try:
            cursor.execute(sql)
            results = cursor.fetchall()  # 返回查询到的所有行数据
            print('结果数据共{}条'.format(cursor.rowcount))
            for row in results:
                print(row)  # 打印每一行数据
        except pymysql.err.ProgrammingError:
            print("发生错误，无法查询数据")


# 范例8
def call_procedure():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='tmp')

    cursor = db.cursor()

    try:
        cursor.callproc('get_maxsal')  # 通过callproc方法调用存储过程
        result = cursor.fetchall()
        print(cursor.rowcount)  # 显示结果的行数
        print(result)
    except pymysql.err.ProgrammingError:
        print('调用错误')
    # 关闭数据库连接
    db.close()


# 范例9
def call_procedure_2():
    with pymysql.connect(host='localhost', user='root', password='123456', database='tmp') as db:
        cursor = db.cursor()

        # 对于out或 inout参数python不支持，随便定义一个值即可，通常使用0
        cursor.callproc('get_sal_1', ('BLAKE', 0))

        # 对于out和inout型参数，是保存在服务器的变量中的，可以通过select语句查询
        # 对应参数的访问格式为 @_存储过程名_0, @_存储过程名_1, 以此类推
        cursor.execute('SELECT @_get_sal_1_0, @_get_sal_1_1')
        print(cursor.fetchall())


if __name__ == '__main__':
    # select_sql_version()    # 查询数据库版本
    # select_sql_version2()  # 查询数据库版本2 -- 通过with as语法连接数据库
    # create_table()    # 通过预处理语句创建表
    # insert_data()  # 插入表中数据
    # delete_data()  # 删除表中数据
    # update_data()  # 更新表中数据
    # select_data()  # 查询表中数据
    # call_procedure()  # 调用存储过程，不带参数版
    call_procedure_2()  # 调用存储过程，参数版
