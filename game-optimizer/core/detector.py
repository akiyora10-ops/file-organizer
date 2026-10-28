"""Detect installed games across launchers (Steam, Epic, etc.)."""

from __future__ import annotations

import json
import os
import re
import winreg
from pathlib import Path
from typing import Iterable

LAUNCHERS = ["Steam", "Epic Games", "Ubisoft Connect", "EA App", "GOG Galaxy",
             "Battle.net", "Riot Client"]


def _reg_query(root, path, name):
    try:
        with winreg.OpenKey(root, path) as key:
            return winreg.QueryValueEx(key, name)[0]
    except Exception:
        return None


def find_steam_root() -> Path | None:
    # Registry
    for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
        for view in (winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY):
            try:
                with winreg.OpenKey(hive, r"Software\Valve\Steam", 0, winreg.KEY_READ | view) as key:
                    val = winreg.QueryValueEx(key, "SteamPath")[0]
                    p = Path(val)
                    if p.exists():
                        return p
            except Exception:
                pass
    # Common paths / drives
    candidates = [Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Steam",
                  Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Steam"]
    for drive in "CDEFG":
        candidates.append(Path(f"{drive}:/steam"))
        candidates.append(Path(f"{drive}:/Steam"))
        candidates.append(Path(f"{drive}:/Program Files (x86)/Steam"))
        candidates.append(Path(f"{drive}:/Program Files/Steam"))
    for p in candidates:
        if p.exists() and ((p / "steam.exe").exists() or (p / "config").exists()):
            return p
    # Search drives shallow
    for drive in "CDEFG":
        root = Path(f"{drive}:/")
        if not root.exists():
            continue
        try:
            for p in root.iterdir():
                if p.is_dir() and p.name.lower() in ("steam", "steamlibrary"):
                    if (p / "steamapps").exists() or (p / "steam.exe").exists():
                        return p
        except Exception:
            continue
    return None


def parse_libraryfolders(root: Path) -> list[Path]:
    libs = [root]
    vdf = root / "steamapps" / "libraryfolders.vdf"
    if not vdf.exists():
        return libs
    text = vdf.read_text(errors="replace")
    for m in re.finditer(r'"path"\s*"([^"]+)"', text):
        p = Path(m.group(1).replace("\\\\", "\\"))
        if p.exists() and p not in libs:
            libs.append(p)
    # Also parse quoted drive paths like "D:\\SteamLibrary"
    for m in re.finditer(r'"[A-Z]":\\\\[^"]*"', text):
        pass
    return libs


def parse_appmanifest(path: Path) -> dict | None:
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None
    name_m = re.search(r'"name"\s*"([^"]+)"', text)
    dir_m = re.search(r'"installdir"\s*"([^"]+)"', text)
    appid_m = re.search(r'"appid"\s*"([^"]+)"', text)
    if not name_m:
        return None
    return {
        "name": name_m.group(1),
        "installdir": dir_m.group(1) if dir_m else None,
        "appid": appid_m.group(1) if appid_m else None,
    }


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
            if info and info.get("name"):
                info["platform"] = "Steam"
                info["library"] = str(lib)
                info["install_path"] = str(steamapps / "common" / (info["installdir"] or ""))
                games.append(info)
    return games


def detect_epic_games() -> list[dict]:
    games = []
    manifests = Path(os.environ.get("ProgramData", r"C:\ProgramData")) / "Epic" / "EpicGamesLauncher" / "Data" / "Manifests"
    if not manifests.exists():
        return games
    for mf in manifests.glob("*.item"):
        try:
            data = json.loads(mf.read_text())
            games.append({
                "name": data.get("DisplayName"),
                "installdir": data.get("InstallLocation"),
                "platform": "Epic",
                "install_path": data.get("InstallLocation"),
            })
        except Exception:
            continue
    return games


def detect_ubisoft() -> list[dict]:
    games = []
    base = Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Ubisoft" / "Ubisoft Game Launcher" / "games"
    # Ubisoft stores installed games under .../games; not trivial; return empty placeholder
    return games


def detect_all() -> list[dict]:
    out = detect_steam_games() + detect_epic_games()
    # de-dup by name
    seen = set()
    uniq = []
    for g in out:
        if g.get("name") and g["name"] not in seen:
            seen.add(g["name"])
            uniq.append(g)
    return uniq

