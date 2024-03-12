from fastapi import FastAPI
from sqlalchemy import func, select
from starlette.responses import JSONResponse

from database.info import Info
from database import async_session
from .constants_api import API

app = FastAPI()


@app.get(API.PROVINCE_COUNT.value)
async def province_count():
    async with async_session() as session:
        results = await session.execute(
            select(
                Info.province_name.label('province'),
                func.count().label('times')
            )
            .group_by(Info.province_name)
            .order_by(func.count().desc())
            .limit(10)
        )
        result_dict_list = [{'province': row[0], 'count': row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)
