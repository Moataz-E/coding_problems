def sequential_search(alist, item):
    for i in range(len(alist)):
        if alist[i] == item:
            return True
    return False
