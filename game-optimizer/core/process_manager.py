"""Process management helpers (Windows)."""

from __future__ import annotations

import subprocess
from typing import Iterable


def list_processes() -> list[dict]:
    try:
        out = subprocess.check_output(["tasklist", "/FO", "CSV", "/NH"], text=True, errors="replace")
    except Exception:
        return []
    rows = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip('"') for p in line.split('","')]
        if len(parts) >= 5:
            rows.append({"name": parts[0], "pid": parts[1], "mem": parts[4]})
    return rows


def kill_process(name: str) -> bool:
    try:
        subprocess.run(["taskkill", "/F", "/IM", name], check=True, capture_output=True)
        return True
    except Exception:
        return False


def set_priority(name: str, priority: str = "high") -> bool:
    # priority: realtime, high, abovenormal, normal, belownormal, low
    level = {"realtime": "realtime", "high": "high", "abovenormal": "abovenormal",
             "normal": "normal", "belownormal": "belownormal", "low": "low"}.get(priority, "high")
    try:
        subprocess.run(["wmic", "process", "where", f'name="{name}"', "CALL", "setpriority", level],
                       check=True, capture_output=True)
        return True
    except Exception:
        return False


def set_affinity(pid: str, mask: int) -> bool:
    try:
        subprocess.run(["powershell", "-Command",
                        f"(Get-Process -Id {pid}).ProcessorAffinity = {mask}"], check=True, capture_output=True)
        return True
    except Exception:
        return False
