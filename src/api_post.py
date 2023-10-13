from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel

from getdata import GetData
from sql_master import SqlMaster
from tools import log_t

app = FastAPI()


class ItemRequest(BaseModel):
    item: str


try:
    @app.post('/api')
    async def start_api(item: ItemRequest, sql=Depends(SqlMaster), get_data=Depends(GetData)):
        get_data.sql_init(sql=sql)
        return get_data.api_select(item.item)

    @app.middleware('http')
    async def log_requests(request: Request, call_next):
        response = await call_next(request)
        str_result = f'{str(request.client)} [{request.method} {str(response.status_code)}] {str(request.url)}'
        log_t(str_result)
        return response
except Exception as e:
    log_t(str(e))
