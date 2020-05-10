def extraLongFactorials(n):
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    return factorial

if __name__ == '__main__':
    n = int(input())
    elf = extraLongFactorials(n)
    print(elf)
