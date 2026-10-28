"""Network optimization helpers."""

from __future__ import annotations

import subprocess


def flush_dns() -> str:
    try:
        subprocess.run("ipconfig /flushdns", shell=True, check=True, capture_output=True)
        return "DNS flushed."
    except Exception as e:
        return f"Failed: {e}"


def reset_winsock() -> str:
    try:
        subprocess.run("netsh winsock reset", shell=True, check=True, capture_output=True)
        return "Winsock reset (reboot required)."
    except Exception as e:
        return f"Failed: {e}"


def ping(host: str = "8.8.8.8", count: int = 4) -> str:
    try:
        out = subprocess.check_output(["ping", "-n", str(count), host], text=True, errors="replace", timeout=20)
        return out
    except Exception as e:
        return f"Failed: {e}"

