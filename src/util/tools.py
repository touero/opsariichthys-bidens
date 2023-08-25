import logging
import os
import json
import random

from src.constants import Server, Host, ProvinceID, Province


def log_t(*args):
    msg = ','.join(args)
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
        log_t(f'find it: {name}')
        with open(name, 'r', encoding='utf-8') as json_f:
            jsonResult = json.load(json_f)
        return jsonResult
    else:
        return []


def save_json(name: str, _list: []):
    if not os.path.exists(name):
        with open(name, 'w', encoding='utf-8') as json_f:
            json_f.write(json.dumps(_list))
            log_t(f'writing json to: {name}')


def turn_to_dict_of_list(dict_args) -> json:
    result = []
    for i in range(0, len(dict_args)):
        itemDict = dict_args.popitem()
        item = {'province': itemDict[0], 'detail': itemDict[1]}
        result.append(item)
    return result


def exist_json(json_path: object):
    def decorator(func):
        def wrapper(*args, **kwargs):
            listResult = get_json(str(json_path))
            if listResult and random.choice([0, 1]):
                log_t(f'is update: 0')
                return listResult
            else:
                log_t(f'is update: 1')
                return func(*args, **kwargs)

        return wrapper

    return decorator


def get_machine_type() -> str:
    temp = Server(os.name)
    log_t(f'machine_type: {temp}')
    if temp is Server.Windows:
        return Host.Local.value
    elif temp is Server.Linux:
        return Host.Server.value


def province_mapping(dictObject: dict, args=0) -> dict:
    province = None
    if args == 0:
        province = ProvinceID
    elif args == 1:
        province = Province
    for item in list(dictObject):
        if item in province.JIANGSU.value:
            dictObject[Province.JIANGSU.value] = dictObject.pop(item)
        elif item in province.GUANGDONG.value:
            dictObject[Province.GUANGDONG.value] = dictObject.pop(item)
        elif item in province.HENAN.value:
            dictObject[Province.HENAN.value] = dictObject.pop(item)
        elif item in province.SHANDONG.value:
            dictObject[Province.SHANDONG.value] = dictObject.pop(item)
        elif item in province.SICHUAN.value:
            dictObject[Province.SICHUAN.value] = dictObject.pop(item)
        elif item in province.HUBEI.value:
            dictObject[Province.HUBEI.value] = dictObject.pop(item)
        elif item in province.HUNAN.value:
            dictObject[Province.HUNAN.value] = dictObject.pop(item)
        elif item in province.ANHUI.value:
            dictObject[Province.ANHUI.value] = dictObject.pop(item)
        elif item in province.HEBEI.value:
            dictObject[Province.HEBEI.value] = dictObject.pop(item)
        elif item in province.ZHEJIANG.value:
            dictObject[Province.ZHEJIANG.value] = dictObject.pop(item)
        elif item in province.LIAONING.value:
            dictObject[Province.LIAONING.value] = dictObject.pop(item)
        elif item in province.JIANGXI.value:
            dictObject[Province.JIANGXI.value] = dictObject.pop(item)
        elif item in province.SHANNXI.value:
            dictObject[Province.SHANNXI.value] = dictObject.pop(item)
        elif item in province.BEIJING.value:
            dictObject[Province.BEIJING.value] = dictObject.pop(item)
        elif item in province.FUJIAN.value:
            dictObject[Province.FUJIAN.value] = dictObject.pop(item)
        elif item in province.YUNNAN.value:
            dictObject[Province.YUNNAN.value] = dictObject.pop(item)
        elif item in province.GUANGXI.value:
            dictObject[Province.GUANGXI.value] = dictObject.pop(item)
        elif item in province.SHANXI.value:
            dictObject[Province.SHANXI.value] = dictObject.pop(item)
        elif item in province.HEILONGJIANG.value:
            dictObject[Province.HEILONGJIANG.value] = dictObject.pop(item)
        elif item in province.CHONGQING.value:
            dictObject[Province.CHONGQING.value] = dictObject.pop(item)
        elif item in province.GUIZHOU.value:
            dictObject[Province.GUIZHOU.value] = dictObject.pop(item)
        elif item in province.JILIN.value:
            dictObject[Province.JILIN.value] = dictObject.pop(item)
        elif item in province.SHANGHAI.value:
            dictObject[Province.SHANGHAI.value] = dictObject.pop(item)
        elif item in province.TIANJIN.value:
            dictObject[Province.TIANJIN.value] = dictObject.pop(item)
        elif item in province.XINJIANG.value:
            dictObject[Province.XINJIANG.value] = dictObject.pop(item)
        elif item in province.NEIMENGGU.value:
            dictObject[Province.NEIMENGGU.value] = dictObject.pop(item)
        elif item in province.GANSU.value:
            dictObject[Province.GANSU.value] = dictObject.pop(item)
        elif item in province.HAINAN.value:
            dictObject[Province.HAINAN.value] = dictObject.pop(item)
        elif item in province.NINGXIA.value:
            dictObject[Province.NINGXIA.value] = dictObject.pop(item)
        elif item in province.XIANGGANG.value:
            dictObject[Province.XIANGGANG.value] = dictObject.pop(item)
        elif item in province.QINGHAI.value:
            dictObject[Province.QINGHAI.value] = dictObject.pop(item)
        elif item in province.XIZANG.value:
            dictObject[Province.XIZANG.value] = dictObject.pop(item)
        elif item in province.AOMEN.value:
            dictObject[Province.AOMEN.value] = dictObject.pop(item)
    return dictObject


def both_count(execute_sql_result: tuple) -> dict:
    result = {}
    for item in execute_sql_result:
        special_name = item[0]
        if special_name in result:
            result[item[0]] += 1
        elif special_name not in result:
            result[item[0]] = 1
    return result


def hava_count(hava: list, not_have: list) -> list:
    count_dual = 0
    for temp in not_have:
        if temp in hava:
            count_dual += 1
    other = len(hava) - count_dual
    result = [{'name': '拥有', 'count': count_dual},
              {'name': '未拥有', 'count': other}]
    return result
