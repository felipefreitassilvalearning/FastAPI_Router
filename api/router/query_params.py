from fastapi import APIRouter

_query_params_router = APIRouter(prefix="/query_params")


@_query_params_router.get("/")
def get(id: int):
    return {"message": "Hello World " + id}

def get_query_params_router() -> APIRouter:
    return _query_params_router
