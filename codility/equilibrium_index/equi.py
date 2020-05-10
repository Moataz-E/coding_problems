def solution(A):
    """Finds the equilibrium index of a list of integers.
    
    Given a zero-indexed array A consisting of N integers, returns any of
    its equilibrium indices. The function should return -1 if no
    equilibrium index exists.

    """
    
    array_length = len(A)

    if (array_length < 1): return -1

    if (array_length < 2): return 0

    #Accumulator to store sum so far
    accumulator = 0

    adjusted_sum = sum(A)

    for i in range(0, (array_length)):

        adjusted_sum -= A[i]

        if (accumulator == adjusted_sum):
            return i

        accumulator += A[i]

    return -1



    
