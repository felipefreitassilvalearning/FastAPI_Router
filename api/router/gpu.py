from fastapi import APIRouter
from api.models.GPU import GPU
from api.models.sample import sample_gpus

_pdf_router = APIRouter(prefix="/pdf")


@_pdf_router.get("/gpu_list")
def get_gpus():
    return sample_gpus

@_pdf_router.get("/gpu/{gpu_id}")
def get_gpu(gpu_id: int):
    if gpu_id >= len(sample_gpus) or gpu_id < 0:
        return {"message": "GPU not found"}
    return sample_gpus[gpu_id]

def get_gpus_router() -> APIRouter:
    return _pdf_router
