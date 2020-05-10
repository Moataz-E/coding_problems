"""
    This program is used to find the sum of the multiples of any numbers up to
    a certain limit. It can accept any number of multiples. Solution is found
    in polynomial time.

    :copyright: (c) 2013 by Moataz Elmasry
"""
import time


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


def prompt(prompt_pause=False):
    """Prompt user for input and choose whether to allow pausing in between."""

    print("Project Euler - Problem 1:\n")
    if prompt_pause:
        time.sleep(1.2)

    print("This program finds the natural sum of all user-defined positive")
    print("multiples below a certain limit. The limit is user-defined.")
    print("----------------------------------------------------------------\n")
    if prompt_pause:
        time.sleep(3)

    # Prompt user for space-separated multiples
    multiples_list = [int(x) for x in input("Enter multiples separated by "
                                            "space:\n").split()]

    # Prompt user for threshold
    limit = int(input("Now, enter the value of the limit:\n"))

    return multiples_list, limit

multiples_list, limit = prompt()
times = 1000
counter = times
start = time.time()
while counter > 0:
    multiples_sum(multiples_list, limit)
    counter -= 1
end = time.time()
print("average elapsed time: " + str(((end-start)/times)*1000))

#print("\nThe answer is:\n", multiples_sum(*prompt()))
