from fastapi import FastAPI, Depends
from getdata import GetData
from sql_master import SqlMaster
from tools import log_t

app = FastAPI()

try:
    @app.get('/api/{item}')
    async def start_api(item, sql=Depends(SqlMaster), get_data=Depends(GetData)):
        get_data.sql_init(sql=sql)
        return get_data.api_select(item)


    @app.middleware('http')
    async def log_requests(requests, call_next):
        response = await call_next(requests)
        str_result = f'{str(requests.client)} [{requests.method} {str(response.status_code)}] {str(requests.url)}'
        log_t(str_result)
        return response
except Exception as e:
    log_t(str(e))
