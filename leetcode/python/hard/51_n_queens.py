"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such
that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.
"""
from typing import List, Tuple

class Board:

    def __init__(self, h, v):
        """Initialize an empty board with h horizontal slots and v vertical."""
        self.h = h
        self.v = v
        self.content = [[0] * h for _ in range(v)]

    def display(self):
        """Converts board to list of strings representation."""
        h_str = [Board.stringify(self.content[s]) for s in range(self.v)]
        return h_str

    @staticmethod
    def stringify(s):
        """Turns a horizontal board segment into string representation."""
        new_str = []
        for c in s:
            if c == 1:
                new_str.append('Q')
            else:
                new_str.append('.')
        return ''.join(new_str)


class NQueens:

    def solve(self, n: int) -> List[List[str]]:
        """Solves the n-queens puzzle for n queensself.

        We represent the baord as an nxn matrix (list of lists) of integers
        where 1 means a queen is placed in that slot and 0 means an empty
        space.

        Leetcode stats:
            Runtime: 152ms
            Memory Usage: 13.8MB

        Args:
            n: integer representing number of queensself.

        Return:
            all distinct solutions to the puzzle for n queens.
        """
        self.board = Board(n ,n)
        sol = []
        self.forward_place(self.board, 0, sol)
        return sol

    def forward_place(self, board: Board, c: int, sol: List[Board]) -> None:
        """Places a piece on the board and checks for validity."""
        if c >= board.h:
            sol.append(board.display())
        else:
            for r in range(board.v):
                if self.confirm_valid(board, (r,c)):
                    board.content[r][c] = 1
                    self.forward_place(board, c+1, sol)
                    board.content[r][c] = 0

    def confirm_valid(self, board: Board, loc: Tuple[int, int]) -> bool:
        """Goes backwards through the board and confirms placement is valid.

        Args:
            board: Board object representing nxn board.
            loc: location on board (row, col) on which Queen is being placed.

        Returns:
            Boolean representing whether Queen condition is valid after
            placement.
        """
        # Check left of the piece
        for c in range(loc[1],-1,-1):
            if board.content[loc[0]][c]: return False
        # Check north-west diagonal of piece
        r, c = loc
        while (r > 0) and (c > 0):
            r -= 1; c -= 1
            if board.content[r][c]: return False
        # check south-west diagonal of piece
        r, c = loc
        while (r < board.v-1) and (c > 0):
            r += 1; c -= 1
            if board.content[r][c]: return False
        return True

nq = NQueens()
nq.solve(4)
