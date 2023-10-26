import pymysql

from pymysql import MySQLError

from constants import DataBaseInfo
from tools import *


class SqlMaster:
    def __init__(self):
        db_info = DataBaseInfo()
        try:
            self.conn = pymysql.connect(host=db_info.host, user=db_info.user, password=db_info.password,
                                        port=db_info.port, database=db_info.database)
        except MySQLError as e:
            log_t(str(e))
            raise e

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

    def get_something_count(self, sql_path: str) -> list:
        result = []
        schools = self.execute_sql(sql_path)
        for school in schools:
            result.append(school[0])
        return result

    def execute_sql(self, sql_path: str) -> tuple:
        if sql_path:
            with open(sql_path, 'r', encoding='utf-8') as file:
                sql_script = file.readline()
            return self.submit_sql_with_return(str(sql_script))

    def __del__(self):
        self.cursor.close()
        self.conn.close()


