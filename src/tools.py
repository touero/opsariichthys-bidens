import logging
import os
import json
import random


def exist_json(json_path: object):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            list_result = Tools.get_json(str(json_path))
            if list_result and random.choice([0, 1]):
                log_t(f'is update: 0')
                return list_result
            else:
                log_t(f'is update: 1')
                return func(*args, **kwargs)

        return wrapper

    return decorator


def log_t(*args):
    msg = ', '.join(args)
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


class Tools:
    @staticmethod
    def get_json(name: str) -> json:
        if os.path.exists(name):
            log_t(f'find it: {name}')
            with open(name, 'r', encoding='utf-8') as json_f:
                json_result = json.load(json_f)
            return json_result
        else:
            return []

    @staticmethod
    def save_json(name: str, _list: []):
        if not os.path.exists(name):
            with open(name, 'w', encoding='utf-8') as json_f:
                json_f.write(json.dumps(_list))
                log_t(f'writing json to: {name}')

    @staticmethod
    def turn_to_dict_of_list(dict_args) -> json:
        result = []
        for i in range(0, len(dict_args)):
            item_dict = dict_args.popitem()
            item = {'province': item_dict[0], 'detail': item_dict[1]}
            result.append(item)
        return result

    @staticmethod
    def both_count(execute_sql_result: tuple) -> dict:
        result = {}
        for item in execute_sql_result:
            special_name = item[0]
            if special_name in result:
                result[item[0]] += 1
            elif special_name not in result:
                result[item[0]] = 1
        return result

    @staticmethod
    def hava_count(hava: list, not_have: list) -> list:
        count_dual = 0
        for temp in not_have:
            if temp in hava:
                count_dual += 1
        other = len(hava) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}]
        return result
