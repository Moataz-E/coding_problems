import os

def bubble_sort(alist):
    """Sort list using n-1 passes."""
    for _ in range(len(alist) - 1):
        for i in range(len(alist) - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [56, 6, 2, 3, 91, 43, 24]
bubble_sort(alist)
alist
