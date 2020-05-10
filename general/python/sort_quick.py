import os

def quick_sort(alist):
    """same as merge sort but doesn't use additional storage"""
    quick_sort_recurs(alist, 0, len(alist)-1)

def quick_sort_recurs(alist, first, last):
    if first > last:
        return
    split = sort_and_split(alist, first, last)
    quick_sort_recurs(alist, first, split-1)
    quick_sort_recurs(alist, split+1, last)

def sort_and_split(alist, first, last):
    pivot = 0
    left_mark = pivot + 1
    right_mark = len(alist) - 1

    while left_mark < right_mark:
        while alist[left_mark] < alist[pivot] and left_mark < right_mark:
            left_mark += 1
        while alist[right_mark] > alist[pivot] and right_mark >= left_mark:
            right_mark -= 1
        alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    # split point found
    alist[pivot], alist[right_mark] = alist[right_mark], alist[pivot]
    return right_mark

alist = [56, 6, 2, 3, 91, 43, 24]
alist = [4]
quick_sort(alist)
alist
