"""
A small frog wants to get to the other side of a river. The frog is initially
located on one bank of the river (position 0) and wants to get to the opposite
bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling
leaves. A[K] represents the position where one leaf falls at time K, measured
in seconds.

The goal is to find the earliest time when the frog can jump to the other side
of the river. The frog can cross only when leaves appear at every position
across the river from 1 to X (that is, we want to find the earliest moment when
all the positions from 1 to X are covered by leaves). You may assume that the
speed of the current in the river is negligibly small, i.e. the leaves do not
change their positions once they fall in the river.

Write a function that, given a non-empty array A consisting of N integers and
integer X, returns the earliest time when the frog can jump to the other side
of the river.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(X: int, A: List[int]) -> int:
    """Find the earliest time when a frog can jump to the other side of a river.

    Codility Score: 100%
    Time Complexity: O(n) where n is length of A.
    """
    leaves = [0] * (X+1)
    leaves_sum = 0
    for t in range(len(A)):
        if A[t] < (X+1) and leaves[A[t]] == 0:
            leaves[A[t]] += 1
            leaves_sum += 1
        if leaves_sum == X: return t
    return -1

assert(solution(5, [1,3,1,4,2,3,5,4]) == 6)
assert(solution(1, [6,9,1]) == 2)
assert(solution(10, [4,2]) == -1)
