"""Tic-tac-toe game logic."""

from __future__ import annotations

import argparse
from typing import Iterable

WINS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]


def check_winner(board: list[str]) -> str | None:
    for a,b,c in WINS:
        if board[a] and board[a]==board[b]==board[c]:
            return board[a]
    if all(board):
        return "draw"
    return None


def move(board: list[str], pos: int, player: str) -> bool:
    if pos < 0 or pos > 8 or board[pos]:
        return False
    board[pos] = player
    return True


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Tic-tac-toe demo.")
    parser.add_argument("moves", nargs="*", type=int)
    args = parser.parse_args(list(argv) if argv is not None else None)
    board = [""]*9
    player = "X"
    for m in args.moves:
        if not move(board, m, player):
            print("invalid move", m); return 1
        w = check_winner(board)
        if w:
            print(w); return 0
        player = "O" if player == "X" else "X"
    print("".join(c or "." for c in board))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
