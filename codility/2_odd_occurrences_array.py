"""
A non-empty array A consisting of N integers is given. The array contains an odd
number of elements, and each element of the array can be paired with another
element that has the same value, except for one element that is left unpaired.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(A: List[int]) -> int:
    """Returns non-duplicate int in an odd array.

    Codility Score: 100%
    Time Complexity: O(n) where n is length of A.
    """
    counter = Counter(A)
    for k,v in counter.items():
        if not(v % 2 == 0):
            return k

assert(solution([2,9,5,2,5]) == 9)
