"""
An array A consisting of N different integers is given. The array contains
integers in the range [1..(N + 1)], which means that exactly one element is
missing.

Your goal is to find that missing element.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(A: List[int]) -> int:
    """find missing integer in a given permutation.

    Codility Score: 100%
    Time Complexity: O(n) where n is length of A.
    """
    counter = Counter(range(1, len(A)+2))
    counter.update(A)
    for k, v in counter.items():
        if v < 2: return k

assert(solution([5,4,1,3]) == 2)
