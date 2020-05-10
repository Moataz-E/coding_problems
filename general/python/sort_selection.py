import os

def selection_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        largest = i
        for j in range(i):
            if alist[j] > alist[largest]:
                largest = j
        alist[largest], alist[i] = alist[i], alist[largest]

alist = [56, 6, 2, 3, 91, 43, 24]
alist = [4]
selection_sort(alist)
alist
