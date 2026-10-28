"""Per-game optimization profiles and system tweaks."""

from __future__ import annotations

PROFILES = {
    "Counter-Strike 2": {
        "launch_options": "-novid -high -threads 8 +fps_max 0 -nojoy",
        "kill_processes": ["chrome.exe", "discord.exe", "spotify.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {"mat_queue_mode": "2", "cl_forcepreload": "1", "r_dynamic": "0"},
    },
    "Valorant": {
        "launch_options": "-high",
        "kill_processes": ["chrome.exe", "discord.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {},
    },
    "Fortnite": {
        "launch_options": "-high -USEALLAVAILABLECORES",
        "kill_processes": ["chrome.exe", "spotify.exe", "epicgameslauncher.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {},
    },
    "Apex Legends": {
        "launch_options": "+mat_letterboxaspectgoal 0 -high",
        "kill_processes": ["chrome.exe", "origin.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {},
    },
    "Call of Duty": {
        "launch_options": "",
        "kill_processes": ["chrome.exe", "battle.net.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {},
    },
    "Minecraft": {
        "launch_options": "-Xmx4G -Xms4G",
        "kill_processes": ["chrome.exe"],
        "priority": "abovenormal",
        "affinity_all": False,
        "config_edits": {},
    },
    "Roblox": {
        "launch_options": "",
        "kill_processes": ["chrome.exe"],
        "priority": "high",
        "affinity_all": True,
        "config_edits": {},
    },
}


def get_profile(name: str) -> dict:
    for key, prof in PROFILES.items():
        if key.lower() in (name or "").lower() or (name or "").lower() in key.lower():
            return prof
    return {"launch_options": "", "kill_processes": [], "priority": "high",
            "affinity_all": True, "config_edits": {}}


def list_profiles() -> list[str]:
    return list(PROFILES.keys())


SYSTEM_TWEAKS = [
    ("Set High Performance power plan", "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"),
    ("Disable Game DVR", 'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f'),
    ("Disable fullscreen optimizations (global)", 'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f'),
]


def apply_system_tweaks(settings: dict | None = None) -> list[str]:
    import subprocess
    from core.config import load
    settings = settings or load()
    enabled = settings.get("system_tweaks", [])
    results = []
    tweak_commands = {
        "High performance power plan": "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
        "Disable Game DVR": 'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f',
        "Disable Xbox Game Bar": 'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f',
        "Disable fullscreen optimizations": 'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f',
        "Disable Nagle (gaming network)": 'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces" /v TcpAckFrequency /t REG_DWORD /d 1 /f',
    }
    for label in enabled:
        cmd = tweak_commands.get(label)
        if not cmd:
            continue
        try:
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
            results.append(f"OK: {label}")
        except Exception as e:
            results.append(f"FAIL: {label} ({e})")
    if not results:
        results.append("No tweaks selected.")
    return results

GAME_PROCESSES = {
    "cs2.exe": "Counter-Strike 2",
    "valorant.exe": "Valorant",
    "valorant-win64-shipping.exe": "Valorant",
    "fortniteclient-win64-shipping.exe": "Fortnite",
    "r5apex.exe": "Apex Legends",
    "cod.exe": "Call of Duty",
    "minecraft.exe": "Minecraft",
    "javaw.exe": "Minecraft",
    "robloxplayerbeta.exe": "Roblox",
}


def running_games() -> list[str]:
    import psutil
    found = []
    for proc in psutil.process_iter(["name"]):
        try:
            name = (proc.info["name"] or "").lower()
            if name in GAME_PROCESSES and GAME_PROCESSES[name] not in found:
                found.append(GAME_PROCESSES[name])
        except Exception:
            continue
    return found
