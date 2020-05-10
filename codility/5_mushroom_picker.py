"""
You are given a non-empty, zero-indexed array A of n (1 ¬ n ¬ 100 000) integers
a 0 , a 1 , . . . , a n−1 (0 ¬ a i ¬ 1 000). This array represents number of
mushrooms growing on the consecutive spots along a road. You are also given
integers k and m (0 ¬ k, m < n).

A mushroom picker is at spot number k on the road and should perform m moves. In
one move she moves to an adjacent spot. She collects all the mushrooms growing
on spots she visits. The goal is to calculate the maximum number of mushrooms
that the mushroom picker can collect in m moves.

Problem is the copyright of Codility Limited.
"""
from typing import List

def prefix_set(A: List[int]) -> List[int]:
    """Calculate prefix set for a given array of integers."""
    ps = [0] * (len(A)+1)
    for i in range(1, len(A) + 1):
        ps[i] = ps[i-1] + A[i-1]
    return ps

def solution(A: List[int], k:int, m:int) -> int:
    """Calculate maximum number of mushrooms that can be picked.

    Using the fact that it wouldn't make sense for the mushroom picker to change
    direction more than once. We loop twice once if mushroom picker
    chooses to go left first, and once if he chose to go right first.

    For each location to the left of the picker (within the m limit), we find
    the maximum distance the picker can go in the opposite direction (right).
    The prefix_set difference for those two locations gives us the sum
    of mushrooms picked in that segment.

    Cost of distance in the direction of travel is counted twice as the
    mushroom picker will have to traverse it twice when going back in the
    opposite direction.

    Time Complexity: O(n) where n is the length of array A.
    """
    ps = prefix_set(A)
    max_mushrooms = 0
    # Iterate through segments if picker goes left first
    for i in range(min(k, m) + 1):
        left_pos = k - i
        backtrace_distance = 2 * i
        right_pos = min(max(k, k + m - 2*i), len(A)-1)
        max_mushrooms = max(max_mushrooms, ps[right_pos+1] - ps[left_pos])
    # Iterate through segments if picker goes right first
    for i in range(min(len(A)-k, m+1)):
        right_pos = k + i
        left_pos = max(0, k - (m - 2*i))
        max_mushrooms = max(max_mushrooms, ps[left_pos] - ps[right_pos])
    return max_mushrooms

assert(solution([4,2,1,3,9,6], 2, 1) == 4)
assert(solution([4,2,1,3,9,6], 2, 2) == 13)
assert(solution([4,2,1,3,9,6], 2, 4) == 19)
assert(solution([4,2,1,3,9,6], 2, 3) == solution([4,2,1,3,9,6], 2, 4))
