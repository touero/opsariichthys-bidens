from fastapi import FastAPI
import uvicorn
from sql_master import SqlMaster
from abc import ABC
from constants import *
import os


class GetData(SqlMaster, ABC):
    def __init__(self):
        super().__init__()

    @property
    def get_province(self):
        sql = "SELECT PROVINCE_NAME FROM info;"
        province_data = self.submit_sql_with_return(sql)
        provinceDict = {}
        for item in province_data:
            province_name = item[0]
            if province_name in provinceDict:
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 0
        return provinceDict

    @property
    def get_dual_class_name(self):
        sql = 'SELECT province_name, dual_class_name FROM info;'
        dual_data = self.submit_sql_with_return(sql)
        provinceDict = {}
        for item in dual_data:
            province_name = item[0]
            dual = item[1]
            if province_name in provinceDict and dual == '双一流':
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 0
        for key in list(provinceDict):
            provinceDict.pop(key) if provinceDict[key] == 0 else ...
        return provinceDict

    @property
    def get_type_name(self):
        sql = 'SELECT type_name FROM info;'
        type_name_data = self.submit_sql_with_return(sql)
        type_nameDict = {}
        for item in type_name_data:
            type_name = item[0]
            if type_name in type_nameDict:
                type_nameDict[type_name] += 1
            elif type_name not in type_nameDict:
                type_nameDict[type_name] = 0
        for type_item in list(type_nameDict):
            type_nameDict.pop(type_item) if type_item == '' else ...
        return type_nameDict


app = FastAPI()
data = GetData()


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
    type_name_count = data.get_type_name
    return type_name_count


def start_task(default_config):
    host = default_config['host']
    port = default_config['port']
    in_server = default_config['in_server']
    for item in API:
        print('http://' + host + ':' + str(port) + item.value)
    if os.name == Server.WINDOWS.value:
        host = Host.LOCAL.value
    elif in_server == Server.LINUX.value:
        host = Host.Server.value
    uvicorn.run(app="api:app", host=host, port=port, reload=True)
