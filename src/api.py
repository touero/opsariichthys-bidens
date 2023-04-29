from fastapi import FastAPI
import uvicorn
from sql_master import SqlMaster
from abc import ABC


class API(SqlMaster, ABC):
    def __init__(self):
        super().__init__()

    def get_province(self):
        sql = "SELECT PROVINCE_NAME FROM info;"
        data = self.submit_sql_with_return(sql)
        province = {}
        for item in data:
            province_name = item[0]
            if province_name in province:
                province[item[0]] += 1
            elif province_name not in province:
                province[item[0]] = 0
        return province


app = FastAPI()
api = API()


@app.get('/')
def error():
    return {"error": 404}


@app.get('/province')
def province():
    provinceJson = api.get_province()
    return provinceJson


def start_task():
    uvicorn.run(app="api:app", port=2518, reload=True)
