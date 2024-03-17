class Driver:
    def __init__(self, option: bool = False):
        self.option = option

    def start(self):
        if self.option:
            from database import create_db
            create_db()
        else:
            import uvicorn
            uvicorn.run(app='api:app', host="0.0.0.0", port=8000, reload=True)
