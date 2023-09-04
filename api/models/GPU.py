# ⦁ Latency
# ⦁ Bandwidth
# ⦁ Number of users already using the GPU
# ⦁ GPU load
# ⦁ GPU VRAM
#   ⦁ Total
#   ⦁ Currently in use
# ⦁ Workload characteristics
#   ⦁ Inference or training
#   ⦁ Required GPU VRAM
#   ⦁ Single or multi-GPU

class VRAM():
    total: float
    in_use: float

class Workload():
    type: str
    required_vram: float
    multi_gpu: bool

class GPU():
    id: int
    name: str
    latency: float
    bandwidth: float
    users: int
    load: float
    vram: dict
    workload: dict
