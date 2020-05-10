"""
A DNA sequence can be represented as a string consisting of the letters A, C, G
and T, which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer. Nucleotides of types
A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going
to answer several queries of the form: What is the minimal impact factor of
nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting
of N characters. There are M queries, which are given in non-empty arrays P and
Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to
find the minimal impact factor of nucleotides contained in the DNA sequence
between positions P[K] and Q[K] (inclusive).

Problem is the copyright of Codility Limited.
"""
from typing import List, Tuple

DNA_CNTR_LOC = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def dna_counter(A: List[int]) -> List[Tuple[int, int, int, int]]:
    """Generates counter where each slot counts how many of each dna type seen.
    """
    ps = [None] * (len(A)+1)
    counter = [0,0,0,0]
    ps[0] = tuple(counter)
    for i in range(1, len(A) + 1):
        counter[DNA_CNTR_LOC[A[i-1]]] += 1
        ps[i] = tuple(counter)
    return ps

def solution(S: str, P: List[int], Q: List[int]) -> List[int]:
    """Find the minimal nucleotide from a range of sequence DNA.

    Codility Score: 100%
    Time Complexity: O(n) where n is the length of string S.
    """
    ps = dna_counter(S)
    min_impact_factors = []
    for p,q in zip(P,Q):
        diff = tuple([ps[q+1][i] - ps[p][i] for i in range(len(ps[q]))])
        if diff[0] > 0: min_impact_factors.append(1)
        elif diff[1] > 0: min_impact_factors.append(2)
        elif diff[2] > 0: min_impact_factors.append(3)
        elif diff[3] > 0: min_impact_factors.append(4)
    return min_impact_factors

assert(dna_counter('C')[-1] == (0,1,0,0))
assert(solution("CAGCCTA", [2,5,0], [4,5,6]) == [2,4,1])
