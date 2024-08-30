from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.engine.result import ChunkedIteratorResult

from database import async_session
from .api_core import ApiCore
from .constants_api import API
from env import PORT
from logs import async_uvicorn_logger, async_sqlalchemy_logger

app = FastAPI()
api_core = ApiCore()


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemRequest(BaseModel):
    key: str


@app.on_event('startup')
async def startup():
    async_uvicorn_logger()
    async_sqlalchemy_logger()


@app.get('/all_api')
async def all_api():
    full_items: list = []
    for api_value, api_desc in API.get_api():
        full_item: dict = {
            "name": api_value,
            "url": f"http://127.0.0.1:{PORT}/api/{api_value}",
            "method": "POST, GET",
            "desc": str(api_desc)
        }
        full_items.append(full_item)
    result = {"name": "all_api", "data": full_items}
    return JSONResponse(content=result)


@app.get('/api/{item}')
async def api(get_item: Request):
    async with async_session() as session:
        select_result = api_core(get_item.path_params['item'])
        return await get_data(select_result, session)


@app.post('/api')
async def api(post_item: ItemRequest):
    async with async_session() as session:
        select_result = api_core(post_item.key)
        return await get_data(select_result, session)


async def get_data(select_result, session):
    if select_result is None:
        return JSONResponse(content={"error": "Invalid request. Invalid item parameter."}, status_code=400)
    if isinstance(select_result, tuple):
        school_ids: ChunkedIteratorResult = await session.execute(select_result[0])
        goals: ChunkedIteratorResult = await session.execute(select_result[1])
        school_id_info: list = [row[0] for row in school_ids.all()]
        school_id_major: list = [row[0] for row in goals.all()]
        have_count: int = 0
        not_count: int = 0
        for school_id in school_id_info:
            if school_id in school_id_major:
                have_count += 1
            else:
                not_count += 1
        return JSONResponse(content={"have_count": have_count, "not_count": not_count})
    results: ChunkedIteratorResult = await session.execute(select_result)
    result_dict_list = [{'param': row[0], 'count': row[1]} for row in results.all()]
    return JSONResponse(content=result_dict_list)
