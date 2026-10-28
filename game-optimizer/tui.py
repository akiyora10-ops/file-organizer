"""Terminal UI for Game Optimizer (Textual)."""

from __future__ import annotations

import threading
import time

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, DataTable, Footer, Header, Input, Label, Static, TabbedContent, TabPane

from core.detector import detect_all
from core.process_manager import list_processes, kill_process, set_priority, boost_pc, system_stats
from core.profiles import get_profile, list_profiles, running_games, apply_system_tweaks
from core.benchmark import system_snapshot


class GameOptimizerTUI(App):
    CSS = """
    Screen { background: #0d1117; }
    TabbedContent { height: 1fr; }
    DataTable { height: 1fr; }
    .box { border: solid #30363d; padding: 1; }
    """
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("b", "boost", "Boost"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with TabbedContent():
            with TabPane("Dashboard", id="dash"):
                yield Static("Game Optimizer Pro - Terminal", id="title")
                yield Static("", id="dash_stats")
                yield Static("", id="dash_games")
                yield Static("", id="dash_running")
            with TabPane("Games", id="games"):
                yield DataTable(id="games_table")
            with TabPane("Processes", id="procs"):
                yield DataTable(id="procs_table")
                yield Horizontal(Button("Refresh", id="proc_refresh"), Button("Kill Top", id="proc_kill"))
            with TabPane("Optimize", id="opt"):
                yield Input(placeholder="Game name", id="opt_input")
                yield Button("Apply Profile", id="opt_apply")
                yield Static("", id="opt_result")
            with TabPane("Monitor", id="mon"):
                yield Static("", id="mon_stats")
                yield Static("", id="mon_gpu")
            with TabPane("Boost", id="boost"):
                yield Button("BOOST NOW", id="boost_btn")
                yield Static("", id="boost_result")
            with TabPane("Network", id="net"):
                yield Button("Flush DNS", id="net_flush")
                yield Button("Ping", id="net_ping")
                yield Static("", id="net_result")
            with TabPane("Cleanup", id="clean"):
                yield Button("Clean Caches", id="clean_btn")
                yield Static("", id="clean_result")
            with TabPane("Tweaks", id="tweaks"):
                yield Button("Apply System Tweaks", id="tweaks_btn")
                yield Static("", id="tweaks_result")
        yield Footer()

    def on_mount(self):
        self._setup_tables()
        self.refresh_all()
        self.set_interval(2, self._tick)

    def _setup_tables(self):
        gt = self.query_one("#games_table", DataTable)
        gt.add_columns("Name", "Platform", "Install Path")
        pt = self.query_one("#procs_table", DataTable)
        pt.add_columns("Name", "PID", "CPU%", "MEM MB")

    def refresh_all(self):
        self._refresh_games()
        self._refresh_procs()
        self._refresh_dash()
        self._refresh_monitor()

    def _refresh_games(self):
        gt = self.query_one("#games_table", DataTable)
        gt.clear()
        for g in detect_all():
            gt.add_row(g.get("name", ""), g.get("platform", ""), g.get("install_path", "") or "")

    def _refresh_procs(self):
        pt = self.query_one("#procs_table", DataTable)
        pt.clear()
        for p in list_processes()[:30]:
            pt.add_row(p["name"], str(p["pid"]), f"{p['cpu']:.1f}", f"{p['mem_mb']:.1f}")

    def _refresh_dash(self):
        snap = system_snapshot()
        mem = snap["mem"]
        self.query_one("#dash_stats", Static).update(
            f"CPU: {snap['cpu']:.1f}% ({snap['cpu_count']} cores) | RAM: {mem['used_gb']}/{mem['total_gb']} GB ({mem['percent']}%) | GPU: {snap['gpu']['name']} {snap['gpu']['util']}%"
        )
        games = detect_all()
        self.query_one("#dash_games", Static).update("Games installed: " + str(len(games)))
        rg = running_games()
        self.query_one("#dash_running", Static).update("Running games: " + (", ".join(rg) if rg else "None"))

    def _refresh_monitor(self):
        snap = system_snapshot()
        mem = snap["mem"]
        gpu = snap["gpu"]
        net = snap["net"]
        self.query_one("#mon_stats", Static).update(
            f"CPU: {snap['cpu']:.1f}%\nRAM: {mem['used_gb']}/{mem['total_gb']} GB ({mem['percent']}%)\nDisk: {snap['disk']['used_gb']}/{snap['disk']['total_gb']} GB\nNet: sent {net['sent_mb']}MB recv {net['recv_mb']}MB"
        )
        self.query_one("#mon_gpu", Static).update(
            f"GPU: {gpu['name']}\nUtilization: {gpu['util']}%\nVRAM: {gpu['mem_used']}/{gpu['mem_total']} MB\nTemp: {gpu['temp']} C"
        )

    def _tick(self):
        self._refresh_dash()
        self._refresh_monitor()

    def on_button_pressed(self, event: Button.Pressed):
        bid = event.button.id
        if bid == "proc_refresh":
            self._refresh_procs()
        elif bid == "proc_kill":
            procs = list_processes()
            if procs:
                kill_process(procs[0]["name"])
                self._refresh_procs()
        elif bid == "opt_apply":
            name = self.query_one("#opt_input", Input).value.strip()
            prof = get_profile(name)
            for proc in prof.get("kill_processes", []):
                kill_process(proc)
            set_priority(name + ".exe", prof.get("priority", "high"))
            self.query_one("#opt_result", Static).update(
                f"Profile: {name}\nLaunch: {prof.get('launch_options')}\nKilled: {', '.join(prof.get('kill_processes', []))}\nPriority: {prof.get('priority')}\nConfig: {prof.get('config_edits')}"
            )
        elif bid == "boost_btn":
            res = boost_pc()
            self.query_one("#boost_result", Static).update("\\n".join(res))
            self._refresh_procs()
        elif bid == "net_flush":
            from core.network import flush_dns
            self.query_one("#net_result", Static).update(flush_dns())
        elif bid == "net_ping":
            from core.network import ping
            self.query_one("#net_result", Static).update(ping())
        elif bid == "clean_btn":
            from core.cleanup import clean_caches
            self.query_one("#clean_result", Static).update("\\n".join(clean_caches()))
        elif bid == "tweaks_btn":
            res = apply_system_tweaks()
            self.query_one("#tweaks_result", Static).update("\n".join(res))

    def action_refresh(self):
        self.refresh_all()

    def action_boost(self):
        res = boost_pc()
        self.notify("Boost complete: " + "; ".join(res)[:80])


def main():
    GameOptimizerTUI().run()


if __name__ == "__main__":
    main()

