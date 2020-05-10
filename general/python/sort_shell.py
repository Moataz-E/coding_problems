import os

def shell_sort(alist):
    shells = len(alist) // 2
    while shells > 0:
        for start in range(shells):
            gap_insertion_sort(alist, start, shells)
        shells //= 2

def gap_insertion_sort(alist, start, gap):
    for i in range(start, len(alist), gap):
        pivot = i
        for j in range(pivot, -1, gap*-1):
            if alist[j] > alist[pivot]:
                alist[j], alist[pivot] = alist[pivot], alist[j]
                pivot = j

alist = [56, 6, 2, 3, 91, 43, 24]
alist = [4]
shell_sort(alist)
alist
