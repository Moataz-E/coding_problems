"""
A non-empty array A consisting of N integers is given. The product of triplet
(P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

Write a function that given a non-empty array A, returns the value of the
maximal product of any triplet.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(A: List[int]) -> int:
    """Calculates the value of the maximal product of any triplet.

    Codility Score: 100%.
    Time Complexity: O(1).
    """
    A.sort()
    # Can have either 0 negative numbers or 2 negative numbers, as 2 negative
    # numbers when multiplied are positive.
    neg_max = A[0] * A[1] * A[-1]
    pos_max = A[-1] * A[-2] * A[-3]
    return neg_max if neg_max > pos_max else pos_max

assert(solution([-3,1,2,-2,5,6]) == 60)
assert(solution([1,2,3]) == 6)
assert(solution([-5,5,-5,4]) == 125)
assert(solution([-5,-2,-8]) == -80)
assert(solution([-4,18,3,-9]) == 648)
