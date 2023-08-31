from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse
from src.getdata import GetData
from util.tools import log_t

app = FastAPI()


@app.get('/api/{item}')
async def start_api(get_data = Depends(GetData)):
    result = get_data.api_select(item)
    return JSONResponse(result)


@app.middleware('http')
async def log_requests(requests, call_next):
    response = await call_next(requests)
    str_result = f'{str(requests.client)} [{requests.method} {str(response.status_code)}] {str(requests.url)}'
    log_t(str_result)
    return response
