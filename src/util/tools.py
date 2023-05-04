import logging
import os
import json


def log_t(msg):
    logger = logging.getLogger('rpa')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename='log/api.log',
                                       encoding='UTF-8')
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.debug(f"{msg}")
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


def get_json(name: str) -> dict:
    if os.path.exists(name):
        log_t(f'找到本地文件:{name}')
        with open(name, 'r', encoding='utf-8') as json_f:
            jsonResult = json.load(json_f)
        return jsonResult
    else:
        return {}


def save_json(name: str, _dict: dict):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as json_f:
            json_f.write(json.dumps(_dict))
            log_t(f'json写入到:{name}')
