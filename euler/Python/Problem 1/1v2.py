"""
    This program is used to find the sum of two user-defined multiples, up to a
    certain limit. Solution is found in linear time.

    :copyright: (c) 2013 by Moataz Elmasry
"""

def multiples_sum(multiple1, multiple2, limit):
    """Finds sum of two multiples up to limit.

    For example, for multiples 2 and 3, and a limit of 10, this function
    will sum the set (0,2,4,6,8,3,9), returning 32.

    Args:
        multiple1: first base multiple to be summed.
        multiple2: second base multiple to be summed.
        limit: upper-bound for multiples to sum.

    Returns:
        Sum of the multiples.
    """

    # Filter out the multiples below the limit, and sum them up
    return sum([number for number in range(0, limit) if (
        (number % multiple1 == 0) or (number % multiple2 == 0))])


# Prompt user for the two multiples
multiple1 = int(input("Please enter the value of the first multiple:\n"))
multiple2 = int(input("Please enter the value of the second multiple:\n"))

# Prompt user for threshold
limit = int(input("Now, enter the value of the limit:\n"))

print("\nThe answer is:\n", multiples_sum(multiple1, multiple2, limit)
