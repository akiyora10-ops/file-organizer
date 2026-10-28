"""Game Optimizer entry point."""

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tui", action="store_true", help="Launch terminal UI")
    args = parser.parse_args()
    if args.tui:
        from tui import main as tui_main
        tui_main()
    else:
        from gui.app import main as gui_main
        gui_main()


if __name__ == "__main__":
    main()
