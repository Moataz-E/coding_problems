import os

def insertion_sort(alist):
    for i in range(len(alist)):
        pivot = i
        for j in range(pivot, -1, -1):
            if alist[j] > alist[pivot]:
                alist[j], alist[pivot] = alist[pivot], alist[j]
                pivot = j

alist = [56, 6, 2, 3, 91, 43, 24]
alist = [4]
insertion_sort(alist)
alist
