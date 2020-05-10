def StairCase(n):
    for i in range(n-1,-1,-1):
        spaces = ' ' * i
        hashes = '#' * (n-i)
        print(spaces + hashes)

_n = int(input())
StairCase(_n)