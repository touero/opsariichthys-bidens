from fastapi import FastAPI, Depends
from sqlalchemy import select
from starlette.responses import JSONResponse
from sqlalchemy.engine.result import ChunkedIteratorResult

from database import async_session
from .api_core import ApiCore
from logs import async_uvicorn_logger

app = FastAPI()


@app.on_event('startup')
async def startup():
    async_uvicorn_logger()


@app.get('/{item}')
async def api(item: str, api_core=Depends(ApiCore)):
    async with async_session() as session:
        select_result: select = api_core.select_real(item)
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
