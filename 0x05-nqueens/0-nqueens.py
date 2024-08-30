#!/usr/bin/env python3
"""
N queens
"""

import sys


def is_safe(board: list, row: int, col: int) -> bool:
    """
    Check if it is safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board: list, col: int, solutions: list) -> bool:
    """
    Solve the N queens problem"""
    if col >= len(board):
        solutions.append([[r, board[r].index(1)] for r in range(len(board))])
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0
    return res

def solve_nqueens(n: int) -> list:
    """Solve the N queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions
