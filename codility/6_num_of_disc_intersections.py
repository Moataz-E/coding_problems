"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A
of N non-negative integers, specifying the radiuses of the discs, is given. The
J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th
discs have at least one common point (assuming that the discs contain their
borders).

Write a function that given an array A describing N discs as explained above,
returns the number of (unordered) pairs of intersecting discs. The function
should return −1 if the number of intersecting pairs exceeds 10,000,000.

Problem is the copyright of Codility Limited.
"""
from typing import List
from bisect import bisect_right

def solution(A: List[int]) -> int:
    """Compute the number of intersections in a sequence of discs.

    Codility Score: 100%.
    Time Complexity: O(n).
    """
    # Variable to track number of intersections found
    intersections = 0
    # Create intervals list. This is basically a list of tuples where each tuple
    # contains the lowest point in the circle along the y-axis, and its
    # corrosponding highest point.
    intervals = sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )
    # Filter all the starting points of each interval
    starts = [i[0] for i in intervals]
    print(starts)
    for i in range(len(starts)):
        # Insert ending into starts list, and count how many items it
        # bisects.
        count = bisect_right(starts, intervals[i][1])
        # Subtract current position from intersections found as this will
        # exclude duplicate intersection points. That is points like (1,3) and
        # (3, 1) only count once. Also, subtract one unit to exclude self
        # intersections. That is points like (3, 3) don't count.
        count -= (i+1)
        intersections += count
        if intersections > 10000000: return -1
    return intersections

assert(solution([1,5,2,1,4,0]) == 11)
print(solution([1,0,0,1,0]))
