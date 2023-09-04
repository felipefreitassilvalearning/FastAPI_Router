sample_gpus = [
    {
        "id": 0,
        "name": "Tesla V100-SXM2-16GB",
        "latency": 0.1,
        "bandwidth": 900,
        "users": 0,
        "load": 0,
        "vram": dict({
            "total": 16,
            "in_use": 0,
        }),
        "workload": dict({
            "type": "inference",   
            "required_vram": 0.5,
            "multi_gpu": False,
        }),
    },
    {
        "id": 1,
        "name": "GeForce RTX 2080 Ti",
        "latency": 0.2,
        "bandwidth": 600,
        "users": 0,
        "load": 0,
        "vram": dict({
            "total": 11,
            "in_use": 0,
        }),
        "workload": dict({
            "type": "training",
            "required_vram": 10,
            "multi_gpu": True,
        }),
    }
]
