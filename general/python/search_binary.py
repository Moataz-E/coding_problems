import os

def binary_search(alist, item):
    s_segment = 0
    e_segment = len(alist) - 1
    while s_segment <= e_segment:
        pivot = (s_segment + e_segment) // 2
        p_item = alist[pivot]
        if p_item == item:
            return True
        elif item < p_item:
            e_segment = pivot - 1
        else:
            s_segment = pivot + 1
    return False

alist = [1, 9, 14, 72, 445, 487, 782, 809, 832, 943]

binary_search(alist, 782)
binary_search(alist, 1)
binary_search(alist, 15)
binary_search(alist, 1000)
