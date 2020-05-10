"""
A non-empty array A consisting of N integers is given. Array A represents
numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... +
A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

Write a function that, given a non-empty array A of N integers, returns the
minimal difference that can be achieved.

Problem is the copyright of Codility Limited.
"""
from typing import List


def solution(A: List[int]) -> int:
    """Find minimum value in a split array.

    Codility Score: 100%
    Time Complexity: O(n) where n is length of A.
    """
    min_abs_diff = -1
    right_sum = 0
    left_sum = sum(A)
    for i in range(len(A)-1):
        right_sum += A[i]
        left_sum -= A[i]
        abs_diff = abs(right_sum - left_sum)
        if min_abs_diff == -1:
            min_abs_diff = abs_diff
        else:
            min_abs_diff = min(min_abs_diff, abs_diff)
    return min_abs_diff

assert(solution([3,1,2,4,3]) == 1)
assert(solution([5,3]) == 2)
