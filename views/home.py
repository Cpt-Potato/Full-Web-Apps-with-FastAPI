from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get("/")
@template()  # (template_file="home/index.pt")
def index(user: str = "anon"):
    return {"user_name": user if user else "anon"}


@router.get("/about")
@template()
def about():
    return {}
