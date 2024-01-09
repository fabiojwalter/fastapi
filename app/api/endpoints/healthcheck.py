import psutil

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    # Server Uptime
    uptime = psutil.boot_time()

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_info = {
        "total": memory.total / (1024**2),
        "available": memory.available / (1024**2),
        "percent": memory.percent,
    }

    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Network Usage
    net_io = psutil.net_io_counters()
    network_info = {
        "bytes_sent": net_io.bytes_sent,
        "bytes_received": net_io.bytes_recv,
    }

    server_info = {
        "status": "OK",
        "message": "Server is running smoothly",
        "uptime": uptime,
        "memory": memory_info,
        "cpu_percent": cpu_percent,
        "network": network_info,
    }
    return server_info
