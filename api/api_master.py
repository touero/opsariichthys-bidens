from fastapi import FastAPI, APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.engine.result import ChunkedIteratorResult

from database import async_session
from .api_core import ApiCore
from logs import async_uvicorn_logger

router = APIRouter()
api_core = ApiCore()


@router.on_event('startup')
async def startup():
    async_uvicorn_logger()


@router.route('/{item}', methods=['GET', 'POST'])
async def api(item: Request):
    async with async_session() as session:
        select_result = api_core(item.path_params['item'])
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
