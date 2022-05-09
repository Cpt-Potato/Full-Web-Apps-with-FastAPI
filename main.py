import fastapi_chameleon
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from data import db_session
from views import account, index, packages

app = FastAPI()

fastapi_chameleon.global_init("templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index.router)
app.include_router(account.router)
app.include_router(packages.router)


@app.on_event("startup")
async def on_startup():
    await db_session.global_init()
