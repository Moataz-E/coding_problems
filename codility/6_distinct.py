"""
Write a function that given an array A consisting of N integers, returns the
number of distinct values in array A.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(A: List[int]) -> int:
    """Find number of distinct elements in an array.

    Codility Score: 100%.
    Time Complexity: O(n).
    """
    counter = Counter(A)
    return len(counter.keys())

assert(solution([2,1,1,2,3,1]) == 3)
assert(solution([]) == 0)
assert(solution([1,2,3,4,5,6,7,8,9]) == 9)
