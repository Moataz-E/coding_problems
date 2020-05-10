def largest_vehicle_type(lane_range, widths):
    """Finds the largest possible vehicle type that can find in service lane.

    Args:
        lane_range: tuple representing entry and exit points of service lane.
        widths: width of each segment in the service lane.

    Returns:
        1 if largest vehicle is a bike, 2 if largest vehicle is a car, and 3 if
        largest vehicle is a truck.
    """
    min_width = 3  # Assume we can fit largest from the start.
    for segment_width in widths[lane_range[0]:lane_range[1]+1]:
        min_width = min(min_width, segment_width)
    return min_width


def prompt():
    """Prompt user for input.

    Returns:
        Tuple whose first element is a list containing integers which represent
        the widths of the service lane and whose second element is a list of
        tuples of all the test cases.
    """
    test_cases_input = []

    freeway_length, num_test_cases = [int(x) for x in input().split(' ')]
    widths_input = [int(x) for x in input().split(' ')]
    for test_case in range(1, num_test_cases+1):
        test_cases_input.append(tuple([int(x) for x in input().split()]))

    return widths_input, test_cases_input


if __name__ == '__main__':
    widths, test_cases = prompt()
    for test_case in test_cases:
        print(largest_vehicle_type(test_case, widths))
