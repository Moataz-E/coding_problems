"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only
once.

Write a function that, given an array A, returns 1 if array A is a permutation
and 0 if it is not.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(A: List[int]) -> int:
    """check whether array A is a permutation.

    Codility Score: 100%
    Time Complexity: O(n) where n is the length of array A.
    """
    counter = Counter(A)
    for x in range(1, len(A)+1):
        if not(counter[x] == 1):
            return 0
    return 1

assert(solution([4,1,3,2]) == True)
assert(solution([9,2]) == False)
assert(solution([15,8,3,14,2,13,12,10,11,9,1,7,5,6,4]) == True)
