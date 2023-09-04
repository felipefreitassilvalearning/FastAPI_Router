from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as start_server

from config import settings
from api.router import main, gpu

def init_app() -> FastAPI:
    app = FastAPI(title=settings.API_TITLE)
    app.include_router(main.get_main_router())
    app.include_router(gpu.get_gpus_router())
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"]
    )
    return app

app = init_app()


if __name__ == "__main__":
    start_server(app,
                host=settings.API_HOST,
                port=settings.API_PORT,
                reload=True)
