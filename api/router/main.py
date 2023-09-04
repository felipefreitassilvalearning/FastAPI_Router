from fastapi import APIRouter

_main_router = APIRouter()


@_main_router.get("/")
def get():
    return {"message": "Hello World"}

def get_main_router() -> APIRouter:
    return _main_router
