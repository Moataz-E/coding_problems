import math


def populate_squares(limit):
    """Populates a pre-computed list of square numbers up to a limit.

    Args:
        limit: largest number that in range.

    Returns:
        List containing all square numbers up to the limit.
    """
    squares = []
    max_squared = int(math.sqrt(limit))
    for number in range(1, max_squared+1):
        squares.append(number*number)
    return squares


def squares_between(start, end, squares):
    """Finds square integers between start and end.

    This function uses a pre-calculated squares list for speedup reasons.

    Args:
        start: start of range for which we have to find squares between.
        end: end of range for which we have to find squares between.
        squares: precomputed list of squares up to a certain limit.

    Returns:
        number of square integers between start and end.
    """
    if start == 1:
        squares_start = 0
    else:
        squares_start = int(math.sqrt(start))

    if squares[squares_start-1] == start:
        squares_start = int(math.sqrt(start)) - 1

    squares_end = int(math.sqrt(end))
    return len([square for square in squares[squares_start:squares_end]])


def prompt():
    """Prompt user for input.

    Returns:
        list containing tuples where ethe first item in the tuple represents
        the start of the range and the second item represents the end of the
        range.
    """
    input_ranges = []
    num_test_cases = int(input())
    for test_case in range(1, num_test_cases+1):
        input_ranges.append(tuple([int(x) for x in input().split()]))

    return input_ranges


if __name__ == '__main__':
    squares_range = prompt()
    max_end = max([x for (_, x) in squares_range])
    squares = populate_squares(max_end)
    for start, end in squares_range:
        print(squares_between(start, end, squares))
