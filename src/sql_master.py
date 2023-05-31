import pymysql
from constants import *
from util.tools import *
from abc import ABC


class SqlMaster(ABC):
    def __init__(self):
        self.conn = pymysql.connect(host=SqlInfo.HOST.value, user=SqlInfo.USER.value,
                                    password=SqlInfo.PASSWORD.value, port=SqlInfo.PORT.value,
                                    database=SqlInfo.DATABASE.value)

        self.cursor = self.conn.cursor()

    def submit_sql_with_return(self, sql: str) -> tuple:
        log_t(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def only_submit_sql(self, sql):
        log_t(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


