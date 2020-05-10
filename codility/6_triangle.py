"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
if 0 ≤ P < Q < R < N and:
    A[P] + A[Q] > A[R],
    A[Q] + A[R] > A[P],
    A[R] + A[P] > A[Q].

Write a function that given an array A consisting of N integers, returns 1 if
there exists a triangular triplet for this array and returns 0 otherwise.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(A: List[int]) -> int:
    """FInds if array contains a triangular triplet.

    Codility Score: 100%.
    Time Complexity: O(n) where n is the length of array A.
    """
    if len(A) < 3: return 0
    A.sort()
    for i in range(2, len(A)):
        cond1 = A[i-2] + A[i-1] > A[i]
        cond2 = A[i-1] + A[i] > A[i-2]
        cond3 = A[i-2] + A[i] > A[i-1]
        if cond1 and cond2 and cond3: return 1
    return 0

assert(solution([10,2,5,1,8,20]) == 1)
assert(solution([1,5]) == 0)
assert(solution([5,90,160]) == 0)
assert(solution([5,3,3]) == 1)
