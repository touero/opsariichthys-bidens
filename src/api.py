from fastapi import FastAPI
import uvicorn
from sql_master import SqlMaster

app = FastAPI()


@app.get('/')
def read_root():
    return {"result": "404"}


class API(SqlMaster):
    def __init__(self):
        super().__init__()

    def start_task(self):
        uvicorn.run(app="api:app", port=2518, reload=True)

