from fastapi import FastAPI
from starlette.responses import JSONResponse
from src.getdata import GetData
from util.tools import log_t

app = FastAPI()


@app.middleware('http')
async def log_requests(requests, call_next):
    response = await call_next(requests)
    str_result = f'{str(requests.client)} [{requests.method} {str(response.status_code)}] {str(requests.url)}'
    log_t(str_result)
    return response


@app.get('/api/{item}')
async def start_api(item: str):
    data = GetData()
    result = data.api_select(item)
    return JSONResponse(result)

