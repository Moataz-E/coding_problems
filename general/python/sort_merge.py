import os

def merge_sort(alist):
    if len(alist) < 2:
        return

    split = len(alist) // 2
    left_half = alist[:split]
    right_half = alist[split:]
    merge_sort(left_half)
    merge_sort(right_half)

    # Two pointers i and j for each of the list halfs.
    # Pointer k to keep track of location in new sorted list
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            alist[k] = left_half[i]
            i += 1
        else:
            alist[k] = right_half[j]
            j += 1
        k += 1

    while (i < len(left_half)):
        alist[k] = left_half[i]
        i += 1
        k += 1

    while (j < len(right_half)):
        alist[k] = right_half[j]
        j += 1
        k += 1


alist = [56, 6, 2, 3, 91, 43, 24]
alist = [4]
merge_sort(alist)
alist
