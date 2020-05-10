"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

 * Each of the digits 1-9 must occur exactly once in each row.
 * Each of the digits 1-9 must occur exactly once in each column.
 * Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
        sub-boxes of the grid.

Empty cells are indicated by the character '.'.
"""
import math
import copy
import itertools
from typing import List, Tuple


class SudokuSolver(object):

    MAX_VALUE = 9

    def valid_placement(self, board: List[List[str]], pos: Tuple[int, int],
        val: str) -> bool:
        """
        pos first element is row and second is column.
        smaller boxes in grid are square root of grid size.
        """
        row = pos[0]
        col = pos[1]
        # Check vertical
        for i in range(len(board)):
            if board[i][col] == val:
                return False
        # Check horizontal
        for i in range(len(board[0])):
            if board[row][i] == val:
                return False
        # Check square
        square_size = int(math.sqrt(len(board)))
        square_row_start = math.floor(row / square_size) * square_size
        square_col_start = math.floor(col / square_size) * square_size
        pos_products = itertools.product(range(square_size), repeat=2)
        for i,j in pos_products:
            if board[square_row_start+i][square_col_start+j] == val:
                return False
        return True

    def get_prev_fill_square(self, board, curr_pos) -> Tuple[int, int]:
        row = curr_pos[0]
        col = curr_pos[1]
        board_rows = len(board)
        board_cols = len(board[0])
        if col == 0:
            prev_col = board_cols - 1
            prev_row = row - 1
        else:
            prev_col, prev_row = col - 1, row
        if self.old_board[prev_row][prev_col] != ".":
            return self.get_prev_fill_square(board, (prev_row, prev_col))
        return (prev_row, prev_col)

    def incr_and_traverse_board(self, board: List[List[str]],
        curr_pos=(0,0)) -> None:
        row = curr_pos[0]
        col = curr_pos[1]
        board_val = board[row][col]
        if self.old_board[row][col] != ".":
            return
        if board_val == ".":
            start = 1
        else:
            start = int(board_val) + 1
        for i in range(start, self.MAX_VALUE + 1):
            if self.valid_placement(board, curr_pos, str(i)):
                board[curr_pos[0]][curr_pos[1]] = str(i)
                break
        else:
            board[curr_pos[0]][curr_pos[1]] = "."
            prev_pos = self.get_prev_fill_square(board, curr_pos)
            self.incr_and_traverse_board(board, prev_pos)
            self.incr_and_traverse_board(board, curr_pos)


    def solve_sudoku(self, board: List[List[str]]) -> None:
        """backtracking algorithm to solve sudoku, modifies board in-place.

        Leetcode stats:
            Runtime: 680ms
            Memory Usage: 13.6MB

        Args:
            board: list of list of strings representing sudoku board.

        Returns:
            Modifies board in-place
        """
        self.old_board = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.incr_and_traverse_board(board, (i,j))


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

ss = SudokuSolver()
ss.solve_sudoku(board)
assert board == solution
