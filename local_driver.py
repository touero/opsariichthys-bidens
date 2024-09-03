import uvicorn
import traceback

from database import create_db
from env import HOST, PORT
from api import API
from logs import log


class LocalDriver:
    def __init__(self):
        ...

    @staticmethod
    def start():
        create_db()
        for api, api_desc in API.get_api():
            log(f"http://127.0.0.1:{PORT}/api/{api}")
        log('If you start fronted, please visit http://127.0.0.1:5173')
        try:
            uvicorn.run(app='api:app', host=HOST, port=PORT, reload=True)
        except Exception as e:
            log(str(e))
            log(traceback.format_exc())
