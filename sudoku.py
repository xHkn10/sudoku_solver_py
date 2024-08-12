import random
import time
from typing import List

from pythonProject import sudoku_funcs


class SudokuSolver:
    class TerminateRecursion(Exception):
        pass

    class UnsolvableSudoku(Exception):
        pass

    @staticmethod
    def valid(board: List[List[int]]) -> bool:
        for row in board:
            check = set()
            for x in row:
                if x == 0:
                    continue
                if x in check or x > 9 or x < 0:
                    return False
                check.add(x)

        for x in range(9):
            check = set()
            for row in board:
                if row[x] == 0:
                    continue
                if row[x] in check or x > 9 or x < 0:
                    return False
                check.add(row[x])

        sub_boxes = zip((0, 0, 0, 3, 3, 3, 6, 6, 6), (0, 3, 6, 0, 3, 6, 0, 3, 6))
        for y, x in sub_boxes:
            check = set()
            for addY in range(3):
                for addX in range(3):
                    if board[y + addY][x + addX] == 0:
                        continue
                    if board[y + addY][x + addX] in check or x > 9 or x < 0:
                        return False
                    check.add(board[y + addY][x + addX])
        return True

    @staticmethod
    def possible(y, x, n: int, board: List[List[int]]) -> bool:
        for i in range(9):
            if board[y][i] == n:
                return False
        for j in range(9):
            if board[j][x] == n:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[y0 + i][x0 + j] == n:
                    return False
        return True

    @staticmethod
    def full(board: List[List[int]]) -> bool:
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    return False
        return True

    @staticmethod
    def solver(board: List[List[int]]) -> None:
        if time.time() - sudoku_funcs.t0 > 1:
            raise SudokuSolver.UnsolvableSudoku
        if SudokuSolver.full(board):
            raise SudokuSolver.TerminateRecursion
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    iterator = list(range(1, 10))
                    random.Random().shuffle(iterator)
                    for n in iterator:
                        if SudokuSolver.possible(y, x, n, board):
                            board[y][x] = n
                            SudokuSolver.solver(board)
                            board[y][x] = 0
                    return
