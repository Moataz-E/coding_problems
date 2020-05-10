"""
    This program is used to find the sum of two user-defined multiples, up to a
    certain limit. Solution is found in constant time, which is achieved by
    using the inclusion-exclusion principle.

    :copyright: (c) 2013 by Moataz Elmasry
"""

def multiples_sum(multiple, limit):
    """Finds sum of one multiple up to limit.

    Args:
        multiple: base multiple to be summed.
        limit: upper-bound for multiples to sum.

    Returns:
        Sum of the multiple up to limit.
    """

    # Sum the number of multiples below the limit, multiply by the multiple
    # to obtain the sum of the multiples.
    return multiple*summation(int(limit / multiple))


def summation(limit):
    """Finds the sum of all real numbers up to limit.

    Args:
        limit: upper-bound for whole real-numbers to sum.

    Returns:
        Sum of real numbers up to limit.
    """

    return limit*((limit + 1) / 2)


# Prompt user for the two multiples
multiple1 = int(input("Please enter the value of the first multiple:\n"))
multiple2 = int(input("Please enter the value of the second multiple:\n"))

# Prompt user for threshold
limit = int(input("Now, enter the value of the limit:\n"))

# Add the sum of both multiples, subtract the sum of the product of both
# multiples as they were counted twice. This is basically the
# inclusion-exclusion principle
print("\nThe answer is:\n", int(multiples_sum(multiple1, limit-1) +
      multiples_sum(multiple2, limit-1) -
      multiples_sum(multiple1*multiple2, limit-1)))
