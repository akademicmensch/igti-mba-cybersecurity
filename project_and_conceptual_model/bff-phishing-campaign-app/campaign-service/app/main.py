from fastapi import FastAPI
from app.api.campaigns import movies
from app.api.db import metadata, database, engine
from app.api.db_gophish import metadata, database, gophishdatabase, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/campaigns/openapi.json", docs_url="/api/v1/campaigns/docs")

@app.on_event("startup")
async def startup():
    await database.connect()
    await gophishdatabase.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await gophishdatabase.disconnect()


app.include_router(movies, prefix='/api/v1/campaigns', tags=['campaigns'])