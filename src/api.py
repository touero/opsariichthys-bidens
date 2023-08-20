from fastapi import FastAPI
import uvicorn
from starlette.responses import JSONResponse

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


def api_select(item: str) -> json:
    result = {}
    if item == API.PROVINCE_COUNT.value:
        result = data.get_province
    elif item == API.DUAL_COUNT.value:
        result = data.get_dual_class_name
    elif item == API.TYPE_COUNT.value:
        result = data.get_type_name
    elif item == API.SPECIAL_COUNT.value:
        result = data.get_special_count
    elif item == API.SCORE_PROVINCE.value:
        result = data.get_score_count
    elif item == API.BIG_DATA_COUNT.value:
        result = data.get_big_data_count
    elif item == API.BIG_DATA_PROVINCE_COUNT.value:
        result = data.get_big_data_province_count
    elif item == API.BIG_DATA_TYPE_COUNT.value:
        result = data.get_big_data_type_count
    elif item == API.BIG_DATA_LEVEL2_COUNT.value:
        result = data.get_big_data_level2_count
    elif item == API.BIG_DATA_LEVEL3_COUNT.value:
        result = data.get_big_data_level3_count
    elif item == API.BIG_DATA_IN_DUAL.value:
        result = data.get_big_data_in_dual
    elif item == API.BIG_DATA_IN_NULL.value:
        result = data.get_big_data_in_null
    elif item == API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value:
        result = data.get_artificial_intelligence_in_dual
    elif item == API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value:
        result = data.get_artificial_intelligence_in_null
    return json.dumps(result)


@app.get('/{item}')
async def start_api(item: str):
    result = api_select(item)
    return JSONResponse(result)


def start_task(default_config):
    all_api = {}
    host = ''
    port = default_config['port']
    log_t(f'当前机器:{os.name}')
    if os.name == Server.WINDOWS.value:
        host = Host.local.value
    elif os.name == Server.LINUX.value:
        host = Host.Server.value
    for index, item in enumerate(API):
        all_api[index+1] = f'http://{host}:{port}/{item.value}'
    log_t(f"all_api =\n {json.dumps(all_api, sort_keys=True, indent=4, separators=(',', ': '))}")
    uvicorn.run(app="api:app", host=host, port=port, reload=True)
