"""
You are given N counters, initially set to 0, and you have two possible
operations on them:
    * increase(X) − counter X is increased by 1,
    * max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive
operations:
    * if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    * if A[K] = N + 1 then operation K is max counter.

Write a function that, given an integer N and a non-empty array A consisting of
M integers, returns a sequence of integers representing the values of the
counters.

Problem is the copyright of Codility Limited.
"""
from typing import List
from collections import Counter

def solution(N: int, A: List[int]) -> List[int]:
    """Calculate the values of counters after applying all alt operations.

    Key approach is we keep track of the maximum value and we only set it on
    each item when we are processing it. At the very end, we go through
    all the elements less than the maximum value and set them as well.

    Codility Score: 100%
    Time Complexity: O(n) where n is the max of N and len(A).
    """
    counters = [0] * (N+1)
    last_max = 0
    max_val = 0
    for o in A:
        if o == N+1:
            max_val = last_max
        else:
            if counters[o] < max_val:
                counters[o] = max_val
            counters[o] += 1
            last_max = max(last_max, counters[o])
    for c in range(len(counters)):
        if counters[c] < max_val:
            counters[c] = max_val
    return counters[1:]

assert(solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2])
assert(solution(2, [1,1,1,3,1,1,1,3]) == [6,6])
