def largest_decent_number(digits):
    """Finds largest decent number.

    Solution exploits the fact that if there are more than two sets of five
    threes, it would be better to replace them with fives, otherwise we have to
    find the number of threes we can fit.

    Args:
        digits: number of digits decent number should consist of.

    Returns:
        largest decent number of size digits or -1 if not possible.
    """
    fives = (digits // 3) * 3
    threes = digits - fives
    needed_threes = 5 - threes

    if threes % 5 == 0:
        return ('5' * fives) + ('3' * threes)
    elif (fives - needed_threes) % 3 == 0 and (digits - needed_threes) > 0:
        new_fives = fives - needed_threes
        new_threes = threes + needed_threes
        return ('5' * new_fives) + ('3' * new_threes)
    elif ((fives - needed_threes - 5) % 3 == 0 and
          (digits - needed_threes - 5) > 0):
        new_fives = fives - needed_threes - 5
        new_threes = threes + needed_threes + 5
        return ('5' * new_fives) + ('3' * new_threes)
    else:
        return -1


def prompt():
    """Prompt user for input.

    Returns:
        list containing number of digits in each decent number.
    """
    decent_number_digits = []
    num_test_cases = int(input())
    for test_case in range(1, num_test_cases+1):
        decent_number_digits.append(int(input()))

    return decent_number_digits


if __name__ == '__main__':
    decent_number_digits = prompt()
    for decent_number_digit in decent_number_digits:
        print(largest_decent_number(decent_number_digit))
