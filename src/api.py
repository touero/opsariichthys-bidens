import traceback

from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse

from local_runner import fish_pond

from constants import RequestType
from get_data import GetData
from tools import log

if not fish_pond:
    from configure_run import fish_pond


app = FastAPI()


class ItemRequest(BaseModel):
    key: str


if RequestType.is_api_task(fish_pond.request_type):
    try:
        if fish_pond.request_type == RequestType.API_POST:
            @app.post('/api')
            async def start_api(item: ItemRequest, get_data=Depends(GetData)):
                result = get_data.api_select(item.key)
                if result is None:
                    return JSONResponse(content={"detail": "Invalid item"}, status_code=400)
                return result
        elif fish_pond.request_type == RequestType.API_GET:
            @app.get('/api/{item}')
            async def start_api(item, get_data=Depends(GetData)):
                result = get_data.api_select(item)
                if result is None:
                    return JSONResponse(content={"detail": "Invalid item"}, status_code=400)
                return result
        else:
            raise TypeError('request type error')
    except Exception as e:
        log(str(e))
        log(traceback.format_exc())
else:
    raise TypeError('request type error')


@app.middleware('http')
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    str_result = f'{str(request.client)} [{request.method} {str(response.status_code)}] {str(request.url)}'
    log(str_result)
    return response
