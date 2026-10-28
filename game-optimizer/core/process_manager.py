"""Process management helpers using psutil."""

from __future__ import annotations

import psutil
from pathlib import Path
from typing import Iterable


def list_processes() -> list[dict]:
    rows = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info", "status"]):
        try:
            info = proc.info
            mem = info["memory_info"].rss if info["memory_info"] else 0
            rows.append({
                "name": info["name"],
                "pid": info["pid"],
                "cpu": info.get("cpu_percent", 0.0),
                "mem_mb": round(mem / 1024 / 1024, 1),
                "status": info.get("status", ""),
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    rows.sort(key=lambda r: r["mem_mb"], reverse=True)
    return rows


def kill_process(name_or_pid) -> bool:
    try:
        if isinstance(name_or_pid, int):
            psutil.Process(name_or_pid).kill()
            return True
        for proc in psutil.process_iter(["name", "pid"]):
            if proc.info["name"].lower() == str(name_or_pid).lower():
                proc.kill()
        return True
    except Exception:
        return False


def set_priority(name_or_pid, priority: str = "high") -> bool:
    level = {"realtime": psutil.REALTIME_PRIORITY_CLASS,
             "high": psutil.HIGH_PRIORITY_CLASS,
             "abovenormal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
             "normal": psutil.NORMAL_PRIORITY_CLASS,
             "belownormal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
             "low": psutil.IDLE_PRIORITY_CLASS}.get(priority.lower(), psutil.HIGH_PRIORITY_CLASS)
    try:
        if isinstance(name_or_pid, int):
            psutil.Process(name_or_pid).nice(level)
            return True
        for proc in psutil.process_iter(["name", "pid"]):
            if proc.info["name"].lower() == str(name_or_pid).lower():
                proc.nice(level)
        return True
    except Exception:
        return False


def set_affinity(pid: int, cpus: list[int]) -> bool:
    try:
        psutil.Process(pid).cpu_affinity(cpus)
        return True
    except Exception:
        return False


def system_stats() -> dict:
    mem = psutil.virtual_memory()
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "cpu_count": psutil.cpu_count(),
        "mem_total_gb": round(mem.total / 1024**3, 2),
        "mem_used_gb": round(mem.used / 1024**3, 2),
        "mem_percent": mem.percent,
    }


def boost_pc() -> list[str]:
    import subprocess
    results = []
    # Kill common bloatware
    bloat = ["chrome.exe", "msedge.exe", "spotify.exe", "discord.exe", "skype.exe",
             "teams.exe", "slack.exe", "onedrive.exe"]
    for b in bloat:
        if kill_process(b):
            results.append(f"Killed {b}")
    # High performance power plan
    try:
        subprocess.run("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c", shell=True, check=True)
        results.append("Power plan: High Performance")
    except Exception as e:
        results.append(f"Power plan failed: {e}")
    # Clear working sets (best effort)
    try:
        subprocess.run("powershell -Command \"Get-Process | ForEach-Object { try { $_.MinWorkingSet = 1MB } catch {} }\"",
                       shell=True, capture_output=True)
        results.append("Trimmed working sets")
    except Exception:
        pass
    # Temp cleanup
    try:
        import tempfile, shutil, glob
        temp = tempfile.gettempdir()
        removed = 0
        for p in Path(temp).glob("*"):
            try:
                if p.is_file() or p.is_symlink():
                    p.unlink()
                elif p.is_dir():
                    shutil.rmtree(p, ignore_errors=True)
                removed += 1
            except Exception:
                pass
        results.append(f"Cleaned temp ({removed} items)")
    except Exception as e:
        results.append(f"Temp cleanup failed: {e}")
    return results
