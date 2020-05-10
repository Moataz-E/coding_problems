"""
A non-empty array A consisting of N integers is given. The consecutive elements
of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

* 0 represents a car traveling east,
* 1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where
0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to
the west.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(A: List[int]) -> int:
    """Returns number of pairs of passing cars.

    We traverse the array and keep track of how many cars travelling east we've
    seen. Every time we come across a car travelling in the oppsite direction
    (west), we ass number of east-bound cars seen to our pairs counter.

    Codility Score: 100%
    Time Complexity: O(n) where n is the length of array A.
    """
    pairs = 0
    east_bound_seen = 0
    for i in range(len(A)):
        if pairs > 1000000000: pairs = -1; break
        if A[i] == 1:
            pairs += east_bound_seen
        else:
            east_bound_seen += 1
    return pairs

assert(solution([0,1,0,1,1]) == 5)
assert(solution([0,0,0,0,0,0,0]) == 0)
assert(solution([0,1,1,1,1,1,1,1,1]) == 8)
assert(solution([1,1,1,1,1,1,1]) == 0)
