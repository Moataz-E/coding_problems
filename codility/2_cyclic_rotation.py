"""
An array A consisting of N integers is given. Rotation of the array means that
each element is shifted right by one index, and the last element of the array is
moved to the first place. For example, the rotation of array
A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index
and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be
shifted to the right K times.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(A: List[int], K: int) -> int:
    """rotates an array to the right by k steps.

    Codility Score: 100%
    Time Complexity: O(n) where n is length of A.
    """
    if len(A) < 1:
        return A
    K = K % len(A)
    Ac = A.copy()
    pivot = len(A) - K
    for i in range(len(A)):
        swap_loc = (i + pivot) % len(A)
        A[i] = Ac[swap_loc]
    return A

assert(solution([3,8,9,7,6], 3) == [9,7,6,3,8])
assert(solution([1,2,3,4], 4) == [1,2,3,4])
