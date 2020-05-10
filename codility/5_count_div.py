"""
Write a function that, given three integers A, B and K, returns the number of
integers within the range [A..B] that are divisible by K.

Problem is the copyright of Codility Limited.
"""

def solution(A: int, B: int, K: int) -> int:
    """Computes number of integers divisible by k in range [A:B].

    Codility Score: 100%
    Time Complexity: O(1).
    """
    # Find first number in A:B divisible by K
    min_div = (A // K) * K
    if min_div < A: min_div += K
    # Find last number in A:B divisible by K
    max_div = (B // K) * K
    if max_div > B: max_div -= K
    # Find number inbetween divisibly by K.
    div_by_k = (max_div - min_div) // K
    return div_by_k + 1

assert(solution(6,11,2) == 3)
assert(solution(0,10,2) == 6)
assert(solution(2,15,32) == 0)
assert(solution(0,0,11) == 1)
assert(solution(20,40,6) == 3)
assert(solution(10,10,5) == 1)
