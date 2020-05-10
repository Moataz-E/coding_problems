"""
Given an array of integers A sorted in non-decreasing order, return an array of
the squares of each number, also in sorted non-decreasing order.
"""
from typing import List

class SortedSquare(object):

    def sorted_squares(self, A: List[int]) -> List[int]:
        """Returns square of each number in list.

        Leetcode stats:
            Runtime: 192ms
            Memory Usage: 14.6MB

        Args:
            List of integers in non-decreasing order.

        Returns:
            Squares of each number in the list in non-decreasing order.
        """
        A.sort(key=abs)
        for i in range(len(A)):
            A[i] = pow(A[i], 2)
        return A

ss = SortedSquare()
A = [-4,-1,0,3,10]
sol = ss.sorted_squares(A)
assert(sol == [0,1,9,16,100])
