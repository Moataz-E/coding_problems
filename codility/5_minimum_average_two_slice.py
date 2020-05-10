"""
A non-empty array A consisting of N integers is given. A pair of integers
(P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the
slice contains at least two elements). The average of a slice (P, Q) is the sum
of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be
precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

Write a function that, given a non-empty array A consisting of N integers,
returns the starting position of the slice with the minimal average. If there
is more than one slice with a minimal average, you should return the smallest
starting position of such a slice.

Problem is the copyright of Codility Limited.
"""
from typing import List

def prefix_set(A: List[int]) -> List[int]:
    """Calculate prefix set for a given array of integers."""
    ps = [0] * (len(A)+1)
    for i in range(1, len(A) + 1):
        ps[i] = ps[i-1] + A[i-1]
    return ps

def solution(A):
    """Find the minimal average of any slice containing at least two elements.

    We use the fact that the only way we can get a new minimum average as we
    traverse the array is if we come across a number that is smaller than
    our current minimum average.

    Codility Score: 100%
    Time Complexity: O(n) where n is the length of array A.
    """
    ps = prefix_set(A)
    min_avg = (A[0] + A[1]) / 2
    min_index = 0
    pivot = 0
    for i in range(1, len(A)):
        average = (ps[i+1] - ps[pivot]) / (i - pivot + 1)
        if average < min_avg: min_index = pivot
        min_avg = min(min_avg, average)
        if A[i] < min_avg: pivot = i
    return min_index


assert(solution([4,2,2,5,1,5,8]) == 1)
assert(solution([10000, -10000]) == 0)
