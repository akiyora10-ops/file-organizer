"""Modern CustomTkinter GUI for game optimizer."""

from __future__ import annotations

import threading
import time
import tkinter as tk

import customtkinter as ctk

from core.detector import detect_all
from core.process_manager import list_processes, kill_process, set_priority, system_stats
from core.profiles import get_profile, list_profiles, apply_system_tweaks
from core.benchmark import system_snapshot

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game Optimizer Pro")
        self.geometry("1100x700")
        self.games = []
        self._build()

    def _build(self):
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)
        for name in ("Games", "Processes", "Optimize", "Monitor", "Boost PC", "System Tweaks"):
            self.tabs.add(name)
        self._games_tab()
        self._processes_tab()
        self._optimize_tab()
        self._monitor_tab()
        self._boost_tab()
        self._tweaks_tab()

    # ---- Games ----
    def _games_tab(self):
        f = self.tabs.tab("Games")
        self.games_box = ctk.CTkTextbox(f, width=900, height=400)
        self.games_box.pack(padx=10, pady=10)
        ctk.CTkButton(f, text="Detect Games", command=self.detect_games).pack()
        self.detect_games()

    def detect_games(self):
        self.games = detect_all()
        self.games_box.delete("1.0", "end")
        if not self.games:
            self.games_box.insert("end", "No games detected.\n")
        else:
            for g in self.games:
                self.games_box.insert("end", f"{g.get('name')}  [{g.get('platform')}]  {g.get('install_path','')}\n")
        from core.profiles import running_games
        rg = running_games()
        self.games_box.insert("end", f"\nRunning games: {', '.join(rg) if rg else 'None'}\n")

    # ---- Processes ----
    def _processes_tab(self):
        f = self.tabs.tab("Processes")
        self.proc_box = ctk.CTkTextbox(f, width=900, height=400)
        self.proc_box.pack(padx=10, pady=10)
        row = ctk.CTkFrame(f)
        row.pack(pady=5)
        ctk.CTkButton(row, text="Refresh", command=self.refresh_procs).pack(side="left", padx=5)
        ctk.CTkButton(row, text="Kill Top Memory", command=self.kill_top).pack(side="left", padx=5)
        self.refresh_procs()

    def refresh_procs(self):
        self.proc_box.delete("1.0", "end")
        for p in list_processes()[:40]:
            self.proc_box.insert("end", f"{p['name']:<30} PID {p['pid']:<8} CPU {p['cpu']:>5.1f}%  MEM {p['mem_mb']:>7.1f}MB\n")

    def kill_top(self):
        procs = list_processes()
        if procs:
            kill_process(procs[0]["name"])
            self.refresh_procs()

    # ---- Optimize ----
    def _optimize_tab(self):
        f = self.tabs.tab("Optimize")
        ctk.CTkLabel(f, text="Game name:").pack(pady=5)
        self.game_entry = ctk.CTkEntry(f, width=400)
        self.game_entry.pack()
        ctk.CTkButton(f, text="Apply Optimization Profile", command=self.apply_profile).pack(pady=10)
        self.profile_box = ctk.CTkTextbox(f, width=900, height=300)
        self.profile_box.pack(padx=10, pady=10)

    def apply_profile(self):
        name = self.game_entry.get().strip()
        prof = get_profile(name)
        # kill background processes
        for proc in prof.get("kill_processes", []):
            kill_process(proc)
        # set priority if game running
        set_priority(name + ".exe", prof.get("priority", "high"))
        self.profile_box.delete("1.0", "end")
        self.profile_box.insert("end", f"=== {name} ===\n")
        self.profile_box.insert("end", f"Launch options: {prof.get('launch_options')}\n")
        self.profile_box.insert("end", f"Killed: {', '.join(prof.get('kill_processes', []))}\n")
        self.profile_box.insert("end", f"Priority: {prof.get('priority')}\n")
        self.profile_box.insert("end", f"Config edits: {prof.get('config_edits')}\n")
        self.profile_box.insert("end", "\nApply launch options in Steam/Epic game properties.\n")

    # ---- Monitor ----
    def _monitor_tab(self):
        f = self.tabs.tab("Monitor")
        self.monitor_label = ctk.CTkLabel(f, text="Starting...", font=ctk.CTkFont(size=16))
        self.monitor_label.pack(pady=20)
        self.gpu_label = ctk.CTkLabel(f, text="", font=ctk.CTkFont(size=14))
        self.gpu_label.pack(pady=5)
        ctk.CTkButton(f, text="Start Live Monitor", command=self.start_monitor).pack(pady=10)
        self._monitoring = False

    def start_monitor(self):
        if self._monitoring:
            return
        self._monitoring = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()

    def _monitor_loop(self):
        while self._monitoring:
            snap = system_snapshot()
            cpu = snap["cpu"]
            mem = snap["mem"]
            gpu = snap["gpu"]
            text = (f"CPU: {cpu:.1f}% ({snap['cpu_count']} cores)   |   "
                    f"RAM: {mem['used_gb']}/{mem['total_gb']} GB ({mem['percent']}%)")
            gpu_text = f"GPU: {gpu['name']}  Util: {gpu['util']}%  VRAM: {gpu['mem_used']}/{gpu['mem_total']} MB  Temp: {gpu['temp']}C"
            self.monitor_label.configure(text=text)
            self.gpu_label.configure(text=gpu_text)
            time.sleep(1)

    # ---- Boost PC ----
    def _boost_tab(self):
        f = self.tabs.tab("Boost PC")
        ctk.CTkLabel(f, text="One-click PC boost for gaming", font=ctk.CTkFont(size=18)).pack(pady=10)
        ctk.CTkButton(f, text="BOOST NOW", command=self.boost_now, height=50, width=300).pack(pady=10)
        ctk.CTkLabel(f, text="Running games detected:").pack(pady=5)
        self.running_label = ctk.CTkLabel(f, text="None")
        self.running_label.pack()
        ctk.CTkButton(f, text="Refresh Running Games", command=self.refresh_running).pack(pady=5)
        self.boost_box = ctk.CTkTextbox(f, width=900, height=300)
        self.boost_box.pack(padx=10, pady=10)
        self.refresh_running()

    def refresh_running(self):
        from core.profiles import running_games
        games = running_games()
        self.running_label.configure(text=", ".join(games) if games else "None")

    def boost_now(self):
        from core.process_manager import boost_pc
        results = boost_pc()
        self.boost_box.delete("1.0", "end")
        for r in results:
            self.boost_box.insert("end", r + "\n")
        self.boost_box.insert("end", "\nBoost complete.\n")
        self.refresh_procs()
        self.refresh_running()

    # ---- System Tweaks ----
    def _tweaks_tab(self):
        f = self.tabs.tab("System Tweaks")
        ctk.CTkLabel(f, text="Apply Windows gaming optimizations (run as admin for best results)").pack(pady=10)
        ctk.CTkButton(f, text="Apply All System Tweaks", command=self.apply_tweaks).pack(pady=10)
        self.tweaks_box = ctk.CTkTextbox(f, width=900, height=300)
        self.tweaks_box.pack(padx=10, pady=10)

    def apply_tweaks(self):
        results = apply_system_tweaks()
        self.tweaks_box.delete("1.0", "end")
        for r in results:
            self.tweaks_box.insert("end", r + "\n")


def main():
    App().mainloop()


if __name__ == "__main__":
    main()

