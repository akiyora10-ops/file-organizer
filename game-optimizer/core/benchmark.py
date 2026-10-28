"""Performance monitoring helpers."""

from __future__ import annotations

import subprocess
import time

import psutil


def cpu_usage() -> float:
    return psutil.cpu_percent(interval=0.1)


def memory_usage() -> dict:
    mem = psutil.virtual_memory()
    return {"total_gb": round(mem.total / 1024**3, 2),
            "used_gb": round(mem.used / 1024**3, 2),
            "percent": mem.percent}


def gpu_usage() -> dict:
    # Try nvidia-smi
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu",
             "--format=csv,noheader,nounits"], text=True, errors="replace", timeout=5)
        parts = [p.strip() for p in out.strip().split(",")]
        if len(parts) >= 5:
            return {"name": parts[0], "util": float(parts[1]), "mem_used": float(parts[2]),
                    "mem_total": float(parts[3]), "temp": float(parts[4])}
    except Exception:
        pass
    return {"name": "N/A", "util": 0, "mem_used": 0, "mem_total": 0, "temp": 0}


def disk_usage(path: str = "C:\\") -> dict:
    u = psutil.disk_usage(path)
    return {"total_gb": round(u.total / 1024**3, 1), "used_gb": round(u.used / 1024**3, 1),
            "percent": u.percent}


def system_snapshot() -> dict:
    return {
        "cpu": cpu_usage(),
        "cpu_count": psutil.cpu_count(),
        "mem": memory_usage(),
        "gpu": gpu_usage(),
        "disk": disk_usage(),
    }


def monitor(duration: int = 5, interval: float = 1.0) -> list[dict]:
    samples = []
    for _ in range(max(1, int(duration / interval))):
        samples.append(system_snapshot())
        time.sleep(interval)
    return samples

