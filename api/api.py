from fastapi import FastAPI
from sqlalchemy import func, select, and_
from starlette.responses import JSONResponse
from logs import async_uvicorn_logger

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


@app.get(API.BIG_DATA_TYPE.value)
async def big_data_type():
    async with async_session() as session:
        results = await session.execute(
            select(Major.type_name.label('type_name'), func.count())
            .where(Major.special_name.like("%数据%"))
            .group_by('type_name')
            .order_by(func.count().desc())
        )
        result_dict_list = [{"school_class": row[0], "count": row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.BIG_DATA_LEVEL2.value)
async def big_data_level2():
    async with async_session() as session:
        results = await session.execute(
            select(Major.level2_name.label('level2_name'), func.count())
            .where(Major.special_name.like("%数据%"))
            .group_by('level2_name')
            .order_by(func.count().desc())
            .limit(5)
        )
        result_dict_list = [{"level_class": row[0], "count": row[1]} for row in results.all()]
        return JSONResponse(content=result_dict_list)


@app.get(API.BIG_DATA_IN_DUAL.value)
async def big_data_in_dual():
    async with async_session() as session:
        dual_school_ids = await session.execute(
            select(Info.school_id, func.count())
            .where(Info.dual_class_name == '双一流')
            .group_by(Info.school_id)
        )
        big_data_school_ids = await session.execute(
            select(Major.school_id, func.count())
            .where(Major.special_name == '数据科学与大数据技术')
            .group_by(Major.school_id)
        )
        school_id_info = [row[0] for row in dual_school_ids.fetchall()]
        school_id_major = [row[0] for row in big_data_school_ids.fetchall()]
        have_count = 0
        not_count = 0
        for school_id in school_id_info:
            if school_id in school_id_major:
                have_count += 1
            else:
                not_count += 1
        return JSONResponse(content={"have_count": have_count, "not_count": not_count})


@app.get(API.BIG_DATA_IN_NULL.value)
async def big_data_in_null():
    async with async_session() as session:
        dual_school_ids = await session.execute(
            select(Info.school_id, func.count())
            .where(Info.dual_class_name == 'null')
            .group_by(Info.school_id)
        )
        big_data_school_ids = await session.execute(
            select(Major.school_id, func.count())
            .where(Major.special_name == '数据科学与大数据技术')
            .group_by(Major.school_id)
        )
        school_id_info = [row[0] for row in dual_school_ids.fetchall()]
        school_id_major = [row[0] for row in big_data_school_ids.fetchall()]
        have_count = 0
        not_count = 0
        for school_id in school_id_info:
            if school_id in school_id_major:
                have_count += 1
            else:
                not_count += 1
        return JSONResponse(content={"have_count": have_count, "not_count": not_count})


@app.get(API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value)
async def artificial_intelligence_in_dual():
    async with async_session() as session:
        dual_school_ids = await session.execute(
            select(Info.school_id, func.count())
            .where(Info.dual_class_name == '双一流')
            .group_by(Info.school_id)
        )
        big_data_school_ids = await session.execute(
            select(Major.school_id, func.count())
            .where(Major.special_name == '人工智能')
            .group_by(Major.school_id)
        )
        school_id_info = [row[0] for row in dual_school_ids.fetchall()]
        school_id_major = [row[0] for row in big_data_school_ids.fetchall()]
        have_count = 0
        not_count = 0
        for school_id in school_id_info:
            if school_id in school_id_major:
                have_count += 1
            else:
                not_count += 1
        return JSONResponse(content={"have_count": have_count, "not_count": not_count})


@app.get(API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value)
async def artificial_intelligence_in_dual():
    async with async_session() as session:
        dual_school_ids = await session.execute(
            select(Info.school_id, func.count())
            .where(Info.dual_class_name == 'null')
            .group_by(Info.school_id)
        )
        big_data_school_ids = await session.execute(
            select(Major.school_id, func.count())
            .where(Major.special_name == '人工智能')
            .group_by(Major.school_id)
        )
        school_id_info = [row[0] for row in dual_school_ids.fetchall()]
        school_id_major = [row[0] for row in big_data_school_ids.fetchall()]
        have_count = 0
        not_count = 0
        for school_id in school_id_info:
            if school_id in school_id_major:
                have_count += 1
            else:
                not_count += 1
        return JSONResponse(content={"have_count": have_count, "not_count": not_count})


@app.on_event('startup')
async def startup():
    async_uvicorn_logger()
