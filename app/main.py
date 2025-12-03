from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API ONLINE"}

app.include_router(router)
