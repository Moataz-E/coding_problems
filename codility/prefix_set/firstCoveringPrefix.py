def solution(A):
    """Finds the first covering prefix of a list of integers

    Given a zero-indexed non-empty list A consisting of N integers, returns the
    first covering prefix of A.

    """

    input_set = set(A)

    #Counter to keep track of index being processed
    counter = 0

    while input_set:
        if A[counter] in input_set:
            input_set.remove(A[counter])

        counter += 1

    return counter-1

