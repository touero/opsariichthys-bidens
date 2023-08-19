from fastapi import FastAPI
import uvicorn

from constants import *
from src.getdata import GetData
from util.tools import *

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
async def province():
    provinceJson = data.get_province
    return provinceJson


@app.get(API.DUAL_COUNT.value)
async def dual_class_count():
    dual_provinceJson = data.get_dual_class_name
    return dual_provinceJson


@app.get(API.TYPE_COUNT.value)
async def type_count():
    type_nameJson = data.get_type_name
    return type_nameJson


@app.get(API.SPECIAL_COUNT.value)
async def special_count():
    special_nameJson = data.get_special_count
    return special_nameJson


@app.get(API.SCORE_PROVINCE.value)
async def score_province_count():
    score_provinceJson = data.get_score_count
    return score_provinceJson


@app.get(API.BIG_DATA_COUNT.value)
async def big_data_count():
    big_dataJson = data.get_big_data_count
    return big_dataJson


@app.get(API.BIG_DATA_PROVINCE_COUNT.value)
async def big_data_province_count():
    big_data_provinceJson = data.get_big_data_province_count
    return big_data_provinceJson


@app.get(API.BIG_DATA_TYPE_COUNT.value)
async def big_data_province_count():
    big_data_typeJson = data.get_big_data_type_count
    return big_data_typeJson


@app.get(API.BIG_DATA_LEVEL2_COUNT.value)
async def big_data_level2_count():
    big_data_level2Json = data.get_big_data_level2_count
    return big_data_level2Json


@app.get(API.BIG_DATA_LEVEL3_COUNT.value)
async def big_data_level3_count():
    big_data_level3Json = data.get_big_data_level3_count
    return big_data_level3Json


@app.get(API.BIG_DATA_IN_DUAL.value)
async def get_big_data_in_dual():
    big_data_in_dualJson = data.get_big_data_in_dual
    return big_data_in_dualJson


@app.get(API.BIG_DATA_IN_NULL.value)
async def get_big_data_in_null():
    big_data_in_nullJson = data.get_big_data_in_null
    return big_data_in_nullJson


@app.get(API.BIG_DATA_IN_NULL.value)
async def get_big_data_in_null():
    big_data_in_nullJson = data.get_big_data_in_null
    return big_data_in_nullJson


@app.get(API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value)
async def get_artificial_intelligence_in_dual():
    artificial_intelligence_in_dualJson = data.get_artificial_intelligence_in_dual
    return artificial_intelligence_in_dualJson


@app.get(API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value)
async def get_artificial_intelligence_in_dual():
    artificial_intelligence_in_nullJson = data.get_artificial_intelligence_in_null
    return artificial_intelligence_in_nullJson


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
