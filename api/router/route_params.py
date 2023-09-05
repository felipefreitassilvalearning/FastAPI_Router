from fastapi import APIRouter

_route_params_router = APIRouter(prefix="/route_params")


@_route_params_router.get("/{id}")
def get(id: int):
    return {"message": "Hello World " + id}

def get_route_params_router() -> APIRouter:
    return _route_params_router
