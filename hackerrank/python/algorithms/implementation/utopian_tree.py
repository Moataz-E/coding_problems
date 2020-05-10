def utopian_tree_height(growth_cycle):
    """Finds the height of a utopian tree after growth cycles

    The Utopian Tree goes through 2 cycles of growth every year. Each spring,
    it doubles in height. Each summer, its height increases by 1 meter.

    Args:
        growth_cycle: number of growth cycles the tree goes through.

    Returns:
        height of tree after growth_cycle cycles have passed.
    """
    height = 1
    for cycle in range(1, growth_cycle+1):
        if cycle % 2 != 0:
            height *= 2
        else:
            height += 1

    return height


def prompt():
    """Prompt user for input.

    Returns:
        list containing number of growth cycles.
    """
    growth_cycles_lst = []
    num_test_cases = int(input())
    for test_case in range(1, num_test_cases+1):
        growth_cycles_lst.append(int(input()))

    return growth_cycles_lst

if __name__ == '__main__':
    growth_cycles = prompt()
    for gc in growth_cycles:
        print(utopian_tree_height(gc))
