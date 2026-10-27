"""Detect installed games (Steam, Epic) on Windows."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable

STEAM_REG = r"HKCU\Software\Valve\Steam"
STEAM_PATHS = [Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Steam",
                Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Steam"]


def find_steam_root() -> Path | None:
    for p in STEAM_PATHS:
        if (p / "steam.exe").exists() or (p / "config").exists():
            return p
    return None


def parse_libraryfolders(root: Path) -> list[Path]:
    libs = [root]
    vdf = root / "steamapps" / "libraryfolders.vdf"
    if not vdf.exists():
        return libs
    text = vdf.read_text(errors="replace")
    for m in re.finditer(r'"path"\s*"([^"]+)"', text):
        p = Path(m.group(1).replace("\\\\", "\\"))
        if p.exists():
            libs.append(p)
    return libs


def parse_appmanifest(path: Path) -> dict | None:
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None
    name_m = re.search(r'"name"\s*"([^"]+)"', text)
    dir_m = re.search(r'"installdir"\s*"([^"]+)"', text)
    if not name_m:
        return None
    return {"name": name_m.group(1), "installdir": dir_m.group(1) if dir_m else None, "manifest": str(path)}


def detect_steam_games() -> list[dict]:
    games = []
    root = find_steam_root()
    if not root:
        return games
    for lib in parse_libraryfolders(root):
        steamapps = lib / "steamapps"
        if not steamapps.exists():
            continue
        for manifest in steamapps.glob("appmanifest_*.acf"):
            info = parse_appmanifest(manifest)
            if info:
                info["platform"] = "Steam"
                info["library"] = str(lib)
                games.append(info)
    return games


def detect_epic_games() -> list[dict]:
    games = []
    manifests = Path(os.environ.get("ProgramData", r"C:\ProgramData")) / "Epic" / "EpicGamesLauncher" / "Data" / "Manifests"
    if not manifests.exists():
        return games
    for mf in manifests.glob("*.item"):
        try:
            import json
            data = json.loads(mf.read_text())
            games.append({"name": data.get("DisplayName"), "installdir": data.get("InstallLocation"),
                          "platform": "Epic", "manifest": str(mf)})
        except Exception:
            continue
    return games


def detect_all() -> list[dict]:
    return detect_steam_games() + detect_epic_games()
