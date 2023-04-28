import pymysql
from constants import *


class SqlMaster:
    def __init__(self):
        self.conn = pymysql.connect(host=SqlInfo.HOST.value, user=SqlInfo.USER.value,
                                    password=SqlInfo.PASSWORD.value, port=SqlInfo.PORT.value,
                                    database=SqlInfo.DATABASE.value)

        self.cursor = self.conn.cursor()

    def submit_sql_with_return(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def only_submit_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        # fixme 连接关闭
        # self.conn.close()

    def insert_into(self, table_name, *args):
        sql = f'insert into {table_name} values{args}'
        print(sql)
        self.only_submit_sql(sql)
