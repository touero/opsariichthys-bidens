import os

from fastapi import FastAPI
import uvicorn
from sql_master import SqlMaster
from abc import ABC
from constants import *
from util.tools import *


class GetData(SqlMaster, ABC):
    def __init__(self):
        super().__init__()

    @property
    def get_province(self) -> dict:
        provinceDict = get_json(str(MyJson.PROVINCE_COUNT.value))
        if provinceDict:
            return provinceDict

        sql = "SELECT PROVINCE_NAME FROM info;"
        province_data = self.submit_sql_with_return(sql)

        for item in province_data:
            province_name = item[0]
            if province_name in provinceDict:
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 1
        save_json(str(MyJson.PROVINCE_COUNT.value), provinceDict)
        return provinceDict

    @property
    def get_dual_class_name(self) -> dict:
        provinceDict = get_json(str(MyJson.DUAL_COUNT.value))
        if provinceDict:
            return provinceDict

        sql = 'SELECT province_name, dual_class_name FROM info;'
        dual_data = self.submit_sql_with_return(sql)

        for item in dual_data:
            province_name = item[0]
            dual = item[1]
            if province_name in provinceDict and dual == '双一流':
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 1
        for key in list(provinceDict):
            provinceDict.pop(key) if provinceDict[key] == 0 else ...
        save_json(str(MyJson.DUAL_COUNT.value), provinceDict)
        return provinceDict

    @property
    def get_type_name(self) -> dict:
        type_nameDict = get_json(str(MyJson.TYPE_COUNT.value))
        if type_nameDict:
            return type_nameDict
        sql = 'SELECT type_name FROM info;'
        type_name_data = self.submit_sql_with_return(sql)
        type_nameDict = {}
        for item in type_name_data:
            type_name = item[0]
            if type_name in type_nameDict:
                type_nameDict[type_name] += 1
            elif type_name not in type_nameDict:
                type_nameDict[type_name] = 1
        for type_item in list(type_nameDict):
            type_nameDict.pop(type_item) if type_item == '' else ...
        save_json(str(MyJson.TYPE_COUNT.value), type_nameDict)
        return type_nameDict

    @property
    def get_special_count(self) -> dict:
        special_nameDict = get_json(str(MyJson.SPECIAL_COUNT.value))
        if special_nameDict:
            return special_nameDict
        sql = 'SELECT special_name FROM major;'
        special_names = self.submit_sql_with_return(sql)

        for special_name in special_names:
            special_name = special_name[0]
            if special_name in special_nameDict:
                special_nameDict[special_name] += 1
            elif special_name not in special_names:
                special_nameDict[special_name] = 1
        save_json(str(MyJson.SPECIAL_COUNT.value), special_nameDict)
        return special_nameDict


app = FastAPI()
data = GetData()


@app.middleware('http')
async def log_requests(requests, call_next):
    response = await call_next(requests)
    str_result = requests.method + ' ' + str(response.status_code) + ' ' + str(requests.client) + ' ' + str(
        requests.url)
    log_t(str_result)
    return response


@app.get(API.PROVINCE_COUNT.value)
def province():
    provinceJson = data.get_province
    return provinceJson


@app.get(API.DUAL_COUNT.value)
def dual_class_count():
    dual_provinceJson = data.get_dual_class_name
    return dual_provinceJson


@app.get(API.TYPE_COUNT.value)
def type_count():
    type_nameJson = data.get_type_name
    return type_nameJson


@app.get(API.SPECIAL_COUNT.value)
def special_count():
    special_nameJson = data.get_special_count
    return special_nameJson


def start_task(default_config):
    host = ''
    port = default_config['port']
    log_t(os.name)
    if os.name == Server.WINDOWS.value:
        host = Host.LOCAL.value
    elif os.name == Server.LINUX.value:
        host = Host.Server.value
    for item in API:
        log_t('http://' + host + ':' + str(port) + item.value)
    uvicorn.run(app="api:app", host=host, port=port, reload=True)
