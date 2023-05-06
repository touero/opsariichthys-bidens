from fastapi import FastAPI
import uvicorn
from sql_master import SqlMaster
from abc import ABC
from constants import *
from util.tools import *
from province_map import province_mapping


class GetData(SqlMaster, ABC):
    def __init__(self):
        super().__init__()
        # fixme is_upload是控制是否更新数据的参数，请尝试集成到default_config中
        self.is_upload = 0

    @property
    def get_province(self) -> json:
        listResult = get_json(str(MyJson.PROVINCE_COUNT.value))
        if listResult:
            return listResult

        sql = "SELECT PROVINCE_NAME AS province,count(*) as times FROM info GROUP BY province ORDER BY times DESC;"
        province_data = self.submit_sql_with_return(sql)
        provinceDict = dict(province_data)
        listResult = turn_to_dict_of_list(provinceDict)
        save_json(str(MyJson.PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    def get_dual_class_name(self) -> json:
        listResult = get_json(str(MyJson.DUAL_COUNT.value))
        if listResult:
            return listResult

        sql = 'SELECT province_name, dual_class_name FROM info where dual_class_name = "双一流";'
        dual_data = self.submit_sql_with_return(sql)
        provinceDict = {}
        for item in dual_data:
            province_name = item[0]
            if province_name in provinceDict:
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 1
        listResult = turn_to_dict_of_list(provinceDict)
        save_json(str(MyJson.DUAL_COUNT.value), listResult)
        return listResult

    @property
    def get_type_name(self) -> json:
        listResult = get_json(str(MyJson.TYPE_COUNT.value))
        if listResult:
            return listResult
        sql = 'SELECT type_name AS type_name,count(*) AS times FROM info GROUP BY type_name ORDER BY times DESC;'
        type_name_data = self.submit_sql_with_return(sql)
        type_nameDict = dict(type_name_data)
        listResult = turn_to_dict_of_list(type_nameDict)
        save_json(str(MyJson.TYPE_COUNT.value), listResult)
        return listResult

    @property
    def get_special_count(self) -> json:
        listResult = get_json(str(MyJson.SPECIAL_COUNT.value))
        if listResult:
            return listResult
        sql = 'SELECT special_name AS special_name,COUNT(*) AS times FROM major GROUP BY special_name ORDER BY times ' \
              'DESC LIMIT 10; '
        special_names = self.submit_sql_with_return(sql)
        special_nameDict = dict(special_names)
        listResult = turn_to_dict_of_list(special_nameDict)
        save_json(str(MyJson.SPECIAL_COUNT.value), listResult)
        return listResult

    @property
    def get_score_count(self) -> json:
        listResult = get_json(str(MyJson.SCORE_PROVINCE.value))
        if listResult:
            return listResult
        sql = 'SELECT province_id AS province_id_count,COUNT(*) AS times FROM score GROUP BY province_id  ORDER BY ' \
              'times DESC'
        score_province = self.submit_sql_with_return(sql)
        score_provinceDict = province_mapping(dict(score_province))
        listResult = turn_to_dict_of_list(score_provinceDict)
        save_json(str(MyJson.SCORE_PROVINCE.value), listResult)
        return listResult


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


@app.get(API.SCORE_PROVINCE.value)
def score_province_count():
    score_provinceJson = data.get_score_count
    return score_provinceJson


def start_task(default_config):
    host = ''
    port = default_config['port']
    log_t(f'当前机器:{os.name}')
    if os.name == Server.WINDOWS.value:
        host = Host.LOCAL.value
    elif os.name == Server.LINUX.value:
        host = Host.Server.value
    for item in API:
        log_t('http://' + host + ':' + str(port) + item.value)
    uvicorn.run(app="api:app", host=host, port=port, reload=True)
