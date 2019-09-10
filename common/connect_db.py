# _*_ coding:utf-8 _*_
import pymysql
from sshtunnel import SSHTunnelForwarder


class ExecuteSQL(object):

    # 传入需要连接的数据库的名称dbname和待执行的sql语句
    def __init__(self, dbname, sql):
        self.dbname = dbname
        self.sql = sql

    def execute_sql(self):
        results = ''
        with SSHTunnelForwarder(
                ("110.43.34.124", 22),  # 跳板机（堡垒机）B配置
                ssh_password="Aiot@2019",
                ssh_username="dev",
                remote_bind_address=("172.31.0.251", 3306)) as server:  # 数据库存放服务器C配置

            # 打开数据库连接
            db_connect = pymysql.connect(host='127.0.0.1',  # 本机主机A的IP（必须是这个）
                                         port=server.local_bind_port,
                                         user="aiotdb",
                                         passwd="aiotdb@pa5sw0rd",
                                         db=self.dbname)  # 需要连接的数据库的名称

            # 使用cursor()方法获取操作游标
            cursor = db_connect.cursor()

            try:
                # 执行SQL语句
                cursor.execute(self.sql)
                # 获取所有记录列表
                # results = cursor.fetchall()
                results = cursor.fetchone()
            except Exception as data:
                print('Error: 执行查询失败，%s' % data)

            db_connect.close()
            return results


class ExecuteSQLAll(object):

    # 传入需要连接的数据库的名称dbname和待执行的sql语句
    def __init__(self, dbname, sql):
        self.dbname = dbname
        self.sql = sql

    def execute_sql(self):
        results = ''
        with SSHTunnelForwarder(
                ("110.43.34.124", 22),  # 跳板机（堡垒机）B配置
                ssh_password="Aiot@2019",
                ssh_username="dev",
                remote_bind_address=("172.31.0.251", 3306)) as server:  # 数据库存放服务器C配置

            # 打开数据库连接
            db_connect = pymysql.connect(host='127.0.0.1',  # 本机主机A的IP（必须是这个）
                                         port=server.local_bind_port,
                                         user="aiotdb",
                                         passwd="aiotdb@pa5sw0rd",
                                         db=self.dbname)  # 需要连接的数据库的名称

            # 使用cursor()方法获取操作游标
            cursor = db_connect.cursor()

            try:
                # 执行SQL语句
                cursor.execute(self.sql)
                # 获取所有记录列表
                # results = cursor.fetchall()
                results = cursor.fetchall()
            except Exception as data:
                print('Error: 执行查询失败，%s' % data)

            db_connect.close()
            return results


if __name__ == '__main__':
    name = "iot_test"
    sql = "SELECT * FROM iot_position_share_record WHERE " \
          "host_user_id = '38715a6d7c0608f7.606065919364653057' AND state = 7 " \
          "AND create_time BETWEEN '2019-8-1 12:00:00' AND '2019-8-30 12:0:0' LIMIT 100;"
    connect = ExecuteSQLAll(name, sql)
    share_id = connect.execute_sql()
    print(len(share_id))
