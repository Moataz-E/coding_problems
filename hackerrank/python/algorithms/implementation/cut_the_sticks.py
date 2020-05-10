def perform_cut(sticks):
    """Perform cut operation on sticks until no sticks remain.

    Args:
        sticks: list containing initial lengths of each stick.

    Returns:
        List of remaining sticks after every cut operation.
    """
    new_sticks = sticks
    smallest_stick = min(sticks)
    remaining_sticks = [len(sticks)]
    while len(new_sticks) > 0:
        new_sticks = [x - smallest_stick for x in new_sticks if
                      x - smallest_stick > 0]
        remaining_sticks.append(len(new_sticks))
        smallest_stick = min(new_sticks or [0])

    return remaining_sticks[:-1]


def prompt():
    """Prompt user for input.

    Returns:
        list containing length of each stick.
    """
    num_test_cases = int(input())
    stick_lengths_input = [int(x) for x in input().split()]
    return stick_lengths_input


if __name__ == '__main__':
    stick_lengths = prompt()
    for x in perform_cut(stick_lengths):
        print(x)
