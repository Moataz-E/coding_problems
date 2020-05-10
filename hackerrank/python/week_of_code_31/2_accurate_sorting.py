def is_sorted(array):
    for n1, n2 in zip(array[:-1], array[1:]):
        if n1 > n2:
            return False
    return True

results = []
q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    swaps = True
    while swaps:
        swaps = False
        for i in range(len(a)-1):
            num = a[i]
            next_num = a[i+1]
            if (next_num < num) and (next_num - num == -1):
                a[i+1] = num
                a[i] = next_num
                swaps = True

    if is_sorted(a):
        results.append("Yes")
    else:
        results.append("No")

for res in results:
    print(res)
