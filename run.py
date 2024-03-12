from fastapi import FastAPI

from database import SessionLocal
from database.info import Info


app = FastAPI()


@app.get("/info")
def get_users():
    db = SessionLocal()
    return db.query(Info).limit(10).all()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
