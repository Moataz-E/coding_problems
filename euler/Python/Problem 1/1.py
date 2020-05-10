"""
    This program is used to find the sum of the multiples of any numbers up to
    a certain limit. It can accept any number of multiples. Solution is found
    in polynomial time.

    :copyright: (c) 2013 by Moataz Elmasry
"""

def multiples_sum(multiples_list, limit):
    """ Finds sum of multiples up to limit.

    For example, for multiples list of [2,3] and a limit of 10, this function
    will sum the set (0,2,4,6,8,3,9), returning 32.

    Args:
        multiples_list: list of base multiples to be summed.
        limit: upper-bound for multiples to sum.

    Returns:
        Sum of the multiples.
    """

    # Initialize set that will contain all products
    products_set = set()

    # Populate products set
    for multiple in multiples_list:
        # Return new set, retaining all previous elements in products_set but
        # with new multiples added.
        products_set |= set(range(0, limit, multiple))

    # Sum products set to obtain final solution
    return sum(products_set)


# Prompt user for space-separated multiples
multiples_list = [int(x) for x in input("Enter multiples separated by "
                                        "space:\n").split()]

# Prompt user for threshold
limit = int(input("Now, enter the value of the limit:\n"))

print("\nThe answer is:\n", multiples_sum(multiples_list, limit))
