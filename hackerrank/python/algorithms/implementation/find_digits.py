def even_divisor(digit_string):
    """Find number of individual digits that can evenly divide digit.

    Args:
        digit_string: string representation of digit we want to find divisors
            for.

    Returns:
        number of individual digits in digit_string that can evenly divide it.
    """
    digit = int(digit_string)
    even_divisors = 0
    for digit_divisor in digit_string:
        digit_divisor = int(digit_divisor)

        if digit_divisor == 0:
            continue
        if digit % digit_divisor == 0:
            even_divisors += 1

    return even_divisors


def prompt():
    """Prompt user for input.

    Returns:
        list containing string representation of/99 input digits.
    """
    input_digits = []
    num_test_cases = int(input())
    for test_case in range(1, num_test_cases+1):
        input_digits.append(input())

    return input_digits


if __name__ == '__main__':
    digits = prompt()
    for digit in digits:
        print (even_divisor(digit))
