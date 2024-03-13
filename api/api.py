from fastapi import FastAPI
from sqlalchemy import func, select, and_
from starlette.responses import JSONResponse

from database.model import Info, Major, Score
from database import async_session
from .constants_api import API

app = FastAPI()


@app.get(API.PROVINCE.value)
async def province():
    async with async_session() as session:
        results = await session.execute(
            select(
                Info.province_name,
                func.count()
            )
            .group_by(Info.province_name)
            .order_by(func.count().desc())
            .limit(10)
        )
        result_dict_list = [{'province': row[0], 'count': row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.DUAL_CLASS.value)
async def dual_class():
    async with async_session() as session:
        results = await session.execute(
            select(
                Info.province_name,
                func.count()
            )
            .where(Info.dual_class_name == "双一流")
            .group_by(Info.province_name)
            .order_by(func.count().desc())
        )
        result_dict_list = [{"province": row[0], "count": row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.TYPE.value)
async def type_():
    async with async_session() as session:
        results = await session.execute(
            select(
                Info.type_name,
                func.count()
            )
            .group_by(Info.type_name)
            .order_by(func.count().desc())
        )
        result_dict_list = [{'type': row[0], 'count': row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.MAJOR.value)
async def major():
    async with async_session() as session:
        results = await session.execute(
            select(
                Major.special_name,
                func.count()
            )
            .group_by(Major.special_name)
            .order_by(func.count().desc())
            .limit(10)
        )
        result_dict_list = [{'major': row[0], 'count': row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.ADMISSIONS.value)
async def admissions():
    async with async_session() as session:
        results = await session.execute(
            select(Score.province_id, func.count())
            .group_by(Score.province_id)
            .order_by(func.count().desc())
        )
        result_dict_list = [{'province': row[0], 'count': row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.BIG_DATA.value)
async def big_data():
    async with async_session() as session:
        results = await session.execute(
            select(
                Major.special_name,
                func.count()
            )
            .where(Major.special_name.like("%数据%"))
            .group_by(Major.special_name)
            .order_by(func.count().desc())
            .limit(10)
        )
        result_dict_list = [{"major": row[0], "count": row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.BIG_DATA_PROVINCE.value)
async def big_data_province():
    async with async_session() as session:
        results = await session.execute(
            select(Info.province_id.label('info_province'), func.count())
            .where(and_(Major.special_name.like("%数据%"), Info.school_id == Major.school_id))
            .group_by('info_province')
            .order_by(func.count().desc())
        )
        result_dict_list = [{"province": row[0], "count": row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)
