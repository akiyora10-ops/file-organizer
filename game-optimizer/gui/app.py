"""Tkinter GUI for game optimizer."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox

from core.detector import detect_all
from core.process_manager import list_processes, kill_process, set_priority
from core.profiles import get_profile, list_profiles
from core.benchmark import cpu_usage, memory_usage


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Optimizer")
        self.geometry("900x600")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self._games_tab()
        self._processes_tab()
        self._optimize_tab()
        self._benchmark_tab()

    def _games_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Games")
        self.games_list = tk.Listbox(frame, width=80)
        self.games_list.pack(fill="both", expand=True, padx=10, pady=10)
        ttk.Button(frame, text="Detect Games", command=self.detect).pack()
        self.detect()

    def detect(self):
        self.games_list.delete(0, tk.END)
        for g in detect_all():
            self.games_list.insert(tk.END, f"{g.get('name')} [{g.get('platform')}]")

    def _processes_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Processes")
        self.proc_list = tk.Listbox(frame, width=80)
        self.proc_list.pack(fill="both", expand=True, padx=10, pady=10)
        btns = ttk.Frame(frame)
        btns.pack()
        ttk.Button(btns, text="Refresh", command=self.refresh_procs).pack(side="left", padx=5)
        ttk.Button(btns, text="Kill Selected", command=self.kill_selected).pack(side="left", padx=5)
        self.refresh_procs()

    def refresh_procs(self):
        self.proc_list.delete(0, tk.END)
        for p in list_processes()[:200]:
            self.proc_list.insert(tk.END, f"{p['name']} (PID {p['pid']}) - {p['mem']}")

    def kill_selected(self):
        sel = self.proc_list.curselection()
        if not sel:
            return
        text = self.proc_list.get(sel[0])
        name = text.split(" (PID")[0]
        if kill_process(name):
            messagebox.showinfo("Killed", name)
            self.refresh_procs()
        else:
            messagebox.showerror("Error", f"Could not kill {name}")

    def _optimize_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Optimize")
        ttk.Label(frame, text="Game name:").pack(pady=5)
        self.game_entry = ttk.Entry(frame, width=40)
        self.game_entry.pack()
        ttk.Button(frame, text="Apply Profile", command=self.apply_profile).pack(pady=5)
        self.profile_text = tk.Text(frame, height=15, width=80)
        self.profile_text.pack(padx=10, pady=10)

    def apply_profile(self):
        name = self.game_entry.get().strip()
        prof = get_profile(name)
        self.profile_text.delete("1.0", tk.END)
        self.profile_text.insert(tk.END, f"Profile for: {name}\n")
        self.profile_text.insert(tk.END, f"Launch options: {prof['launch_options']}\n")
        self.profile_text.insert(tk.END, f"Kill processes: {', '.join(prof['kill_processes'])}\n")
        self.profile_text.insert(tk.END, f"Priority: {prof['priority']}\n")
        self.profile_text.insert(tk.END, f"Config edits: {prof['config_edits']}\n")
        for proc in prof["kill_processes"]:
            kill_process(proc)
        messagebox.showinfo("Done", "Profile applied (processes killed).")

    def _benchmark_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Benchmark")
        self.bench_label = ttk.Label(frame, text="CPU/Memory")
        self.bench_label.pack(pady=20)
        ttk.Button(frame, text="Sample", command=self.sample).pack()

    def sample(self):
        self.bench_label.config(text=f"CPU: {cpu_usage()}%  |  MEM: {memory_usage()['percent']}%")


def main():
    App().mainloop()


if __name__ == "__main__":
    main()
