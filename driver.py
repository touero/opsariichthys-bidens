class Driver:
    def __init__(self, option: bool = False):
        self.option = option

    def start(self):
        if self.option:
            from database import create_db
            create_db()
        else:
            import uvicorn
            from env import HOST, PORT
            from api import API
            from logs import log
            for api in API.get_api():
                log(f"http://127.0.0.1:{PORT}/{api}")
            uvicorn.run(app='api:app', host=HOST, port=PORT, reload=True)
