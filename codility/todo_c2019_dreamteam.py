"""
A company has employed N developers (numbered from 0 to N−1) and wants to divide
them into two teams. The first is a front-end team with F developers. The second
is a back-end team with N−F developers. If the K-th developer is assigned to
the front-end team then their contribution is A[K], and if they are assigned to
the back-end team then their contribution is B[K]. What is the maximum sum of
contributions the company can achieve?

Write a function that given two arrays A, B (consisting of N integers each) and
the integer F, returns the maximum sum of contributions the company can achieve.

Problem is the copyright of Codility Limited.
"""
from typing import List

def solution(A: List[int], B: List[int], F: int) -> int:
    """Divide developers into two teams to maximize their total contribution.

    """
    B_num = len(A) - F
    Ai_map = {}
    for i in range(len(A)):
        if A[i] in Ai_map:
            Ai_map[A[i]].add(i)
        else:
            Ai_map[A[i]] = set([i])
    Bi_map = {}
    for i in range(len(B)):
        if B[i] in Bi_map:
            Bi_map[B[i]].append(i)
        else:
            Bi_map[B[i]] = [i]
    Ai = [(tuple(v), k) for k,v in Ai_map.items()]
    Bi = [(tuple(v), k) for k,v in Bi_map.items()]
    Ai_sorted = sorted(Ai, key=lambda x: x[1])
    Bi_sorted = sorted(Bi, key=lambda x: x[1])
    Fs, Bs = set(), set()
    computed = 0
    cond = lambda a,b,x: b[x] <= a[x]
    cond2 = lambda a,b,x: True
    while len(Fs) < F:
        remaining_Fs = F - len(Fs)
        if len(A) - computed <= remaining_Fs:
            cond = cond2
        if not Ai_sorted: break
        ies, F_dev = Ai_sorted.pop()
        if  len(A) - computed <= len(ies):
            cond = cond2
        min_i = min([(i, B[i]) for i in ies], key=lambda x: x[1])[0]
        computed += 1
        if cond(A,B,min_i):
            Fs.add(min_i)
        remaining_ies = set(i for i in ies if i != min_i)
        if remaining_ies: Ai_sorted.append((remaining_ies, F_dev))
    while len(Bs) < B_num:
        ies, B_dev = Bi_sorted.pop()
        for i in ies:
            if i not in Fs: Bs.add(i)
    return sum([A[i] for i in Fs]) + sum(B[i] for i in Bs)

print(solution([7,1,4,4], [5,3,4,3], 2))
print(solution([5,5,5], [5,5,5], 1))
print(solution([4, 2, 1], [2, 5, 3], 2))
print(solution([10,10,10,4000], [120,30,100,70], 3))
