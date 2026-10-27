"""Per-game optimization profiles."""

from __future__ import annotations

PROFILES = {
    "Counter-Strike 2": {
        "launch_options": "-novid -high -threads 8 +fps_max 0",
        "config_edits": {"mat_queue_mode": "2", "cl_forcepreload": "1"},
        "kill_processes": ["chrome.exe", "discord.exe"],
        "priority": "high",
    },
    "Valorant": {
        "launch_options": "-high",
        "config_edits": {},
        "kill_processes": ["chrome.exe"],
        "priority": "high",
    },
    "Fortnite": {
        "launch_options": "-high -USEALLAVAILABLECORES",
        "config_edits": {},
        "kill_processes": ["chrome.exe", "spotify.exe"],
        "priority": "high",
    },
}


def get_profile(name: str) -> dict:
    for key, prof in PROFILES.items():
        if key.lower() in name.lower() or name.lower() in key.lower():
            return prof
    return {"launch_options": "", "config_edits": {}, "kill_processes": [], "priority": "high"}


def list_profiles() -> list[str]:
    return list(PROFILES.keys())
