"""Clean game caches and shader caches."""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Iterable


CACHE_PATHS = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "D3DSCache",
    Path(os.environ.get("LOCALAPPDATA", "")) / "NVIDIA" / "DXCache",
    Path(os.environ.get("LOCALAPPDATA", "")) / "NVIDIA" / "GLCache",
    Path(os.environ.get("APPDATA", "")) / "discord" / "Cache",
    Path(os.environ.get("TEMP", "")),
]


def clean_caches() -> list[str]:
    results = []
    for p in CACHE_PATHS:
        if not p.exists():
            continue
        removed = 0
        try:
            for item in p.iterdir():
                try:
                    if item.is_file() or item.is_symlink():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item, ignore_errors=True)
                    removed += 1
                except Exception:
                    pass
            results.append(f"Cleaned {p} ({removed} items)")
        except Exception as e:
            results.append(f"Failed {p}: {e}")
    return results


def clean_steam_shader_cache(steam_root: str) -> list[str]:
    results = []
    root = Path(steam_root)
    shader = root / "appcache" / "shadercache"
    if shader.exists():
        try:
            shutil.rmtree(shader)
            shader.mkdir(parents=True, exist_ok=True)
            results.append("Cleared Steam shader cache.")
        except Exception as e:
            results.append(f"Failed: {e}")
    else:
        results.append("No Steam shader cache found.")
    return results
PY