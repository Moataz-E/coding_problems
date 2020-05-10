"""
Given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(A: List[int]) -> int:
    """Find smallest positive integer that doesn't occur in a given sequence.

    Codility Score: 100%
    Time Complexity: O(n) where n is the maximum integer in A.
    """

    # If all ints in a list are negative, return 1
    pos_detected = False
    for i in A:
        if i > 0: pos_detected = True; break;
    if not pos_detected: return 1

    max_val = max(A)
    counter = Counter(A)
    for i in range(1, max_val):
        if abs(i) not in counter:
            return i
    return max_val+1


assert(solution([1, 3, 6, 4, 1, 2]) == 5)
assert(solution([1,2,3]) == 4)
assert(solution([-1,-3]) == 1)
assert(solution([4, 5, 6, 2]) == 1)
