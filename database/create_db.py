import os
import sqlite3
import traceback

from logs import log


def create_db():
    log('checking if the sqlite database already exists')
    if os.path.exists('database/all_school.db'):
        log('sqlite database already exists, skipping creation')
        return

    log('creating the sqlite database')
    connection = sqlite3.connect('database/all_school.db')
    with open('database/all_school_sqlite.sql', 'r', encoding='utf-8') as f:
        sql_commands = f.read()
    try:
        log('waiting database to be created')
        cursor = connection.cursor()
        cursor.executescript(sql_commands)
    except Exception as e:
        log(traceback.format_exc())
        log(repr(e))
    finally:
        connection.commit()
        connection.close()
        log('creating the database finish')
