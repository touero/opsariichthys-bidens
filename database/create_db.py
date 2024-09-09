import sqlite3
import traceback

from pathlib import Path
from logs import log


db_path = Path('database/all_school.db')


def create_db():
    sqlite_path = Path('database/all_school_sqlite.sql')
    if db_path.exists():
        log('Checking sqlite database already exists, skipping creation.')
        return

    log(f'Reading the {sqlite_path} to creating the sqlite database.')
    connection = sqlite3.connect(db_path)
    with open(sqlite_path, 'r', encoding='utf-8') as f:
        sql_commands = f.read()
    try:
        log('Waiting database to be created.')
        cursor = connection.cursor()
        cursor.executescript(sql_commands)
        log(f'Creating the database successfully in {db_path}.')
    except Exception as e:
        log(traceback.format_exc())
        log(repr(e))
    finally:
        connection.commit()
        connection.close()
