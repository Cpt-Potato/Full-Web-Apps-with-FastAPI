from fastapi import APIRouter
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.index_viewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = APIRouter()


@router.get("/")
@template()
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()

    return vm.to_dict()


@router.get("/about")
@template()
def about(request: Request):
    vm = ViewModelBase(request)

    return vm.to_dict()
