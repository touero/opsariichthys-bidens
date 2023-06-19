import pymysql
from constants import *
from util.tools import *
from abc import ABC


class SqlMaster:
    def __init__(self):
        self.conn = pymysql.connect(host=SqlInfo.HOST.value, user=SqlInfo.USER.value,
                                    password=SqlInfo.PASSWORD.value, port=SqlInfo.PORT.value,
                                    database=SqlInfo.DATABASE.value)

        self.cursor = self.conn.cursor()

    def submit_sql_with_return(self, sql: str) -> tuple:
        log_t(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def only_submit_sql(self, sql: str):
        log_t(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def get_school_id(self, sql: str) -> str:
        start_suffix = 'school_id="args"'
        result = ''
        schools = self.submit_sql_with_return(sql)
        for index, school_id in enumerate(schools):
            temp = start_suffix.replace('args', school_id[0])
            if index == 0:
                result = temp
            elif index == len(schools):
                result += temp
            else:
                result = result + ' ' + 'or' + ' ' + temp
        return result

    def get_something_count(self, sql: str) -> list:
        result = []
        schools = self.submit_sql_with_return(sql)
        for school in schools:
            result.append(school[0])
        return result

    def __del__(self):
        self.cursor.close()
        self.conn.close()


