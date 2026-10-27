"""Performance monitoring helpers."""

from __future__ import annotations

import subprocess
import time


def cpu_usage() -> float:
    try:
        out = subprocess.check_output(["wmic", "cpu", "get", "loadpercentage"], text=True, errors="replace")
        for line in out.splitlines():
            line = line.strip()
            if line.isdigit():
                return float(line)
    except Exception:
        pass
    return 0.0


def memory_usage() -> dict:
    try:
        out = subprocess.check_output(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize", "/VALUE"], text=True, errors="replace")
        data = {}
        for line in out.splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                data[k.strip()] = v.strip()
        total = int(data.get("TotalVisibleMemorySize", 0))
        free = int(data.get("FreePhysicalMemory", 0))
        used = total - free
        return {"total_kb": total, "used_kb": used, "percent": round(used / total * 100, 1) if total else 0}
    except Exception:
        return {"total_kb": 0, "used_kb": 0, "percent": 0}


def monitor(duration: int = 5, interval: float = 1.0) -> list[dict]:
    samples = []
    for _ in range(int(duration / interval)):
        samples.append({"cpu": cpu_usage(), "mem": memory_usage()["percent"], "t": time.time()})
        time.sleep(interval)
    return samples
