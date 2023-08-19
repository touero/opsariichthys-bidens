import logging
import os
import json

from src.constants import MyJson


def log_t(msg):
    logger = logging.getLogger('api')
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


def get_json(name: str) -> json:
    if os.path.exists(name):
        log_t(f'找到本地文件:{name}')
        with open(name, 'r', encoding='utf-8') as json_f:
            jsonResult = json.load(json_f)
        return jsonResult
    else:
        return []


def save_json(name: str, _list: []):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as json_f:
            json_f.write(json.dumps(_list))
            log_t(f'json写入到:{name}')


def turn_to_dict_of_list(dict_args) -> json:
    result = []
    for i in range(0, len(dict_args)):
        itemDict = dict_args.popitem()
        item = {'province': itemDict[0], 'detail': itemDict[1]}
        result.append(item)
    return result


def exist_json(json_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            listResult = get_json(str(json_path))
            if listResult:
                return listResult
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
