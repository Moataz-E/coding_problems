"""
A small frog wants to get to the other side of the road. The frog is currently
located at position X and wants to get to a position greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its
target.

Problem is the copyright of Codility Limited.
"""
import os

def solution(X: int, Y: int, D: int) -> int:
    """calculate minimum jumps needed by frog to cover distance.

    Codility Score: 100%.
    Time Complexity: O(1).
    """
    distance = (Y - X)
    if distance % D == 0:
        return distance // D
    else:
        return (distance // D) + 1

assert(solution(10,85,30) == 3)
assert(solution(90,105,400) == 1)
assert(solution(10,20,10) == 1)
