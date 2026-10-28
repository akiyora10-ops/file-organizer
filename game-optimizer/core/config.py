"""User settings for Game Optimizer."""

from __future__ import annotations

import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")

DEFAULTS = {
    "bloat_processes": ["chrome.exe", "msedge.exe", "spotify.exe", "discord.exe",
                        "skype.exe", "teams.exe", "slack.exe", "onedrive.exe"],
    "auto_boost": True,
    "boost_clear_temp": True,
    "boost_trim_working_sets": True,
    "boost_power_plan": True,
    "system_tweaks": [
        "High performance power plan",
        "Disable Game DVR",
        "Disable Xbox Game Bar",
        "Disable fullscreen optimizations",
    ],
    "priority_map": {},
}


def load() -> dict:
    if SETTINGS_FILE.exists():
        try:
            data = json.loads(SETTINGS_FILE.read_text())
            merged = DEFAULTS.copy()
            merged.update(data)
            return merged
        except Exception:
            pass
    return DEFAULTS.copy()


def save(settings: dict) -> None:
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2))

