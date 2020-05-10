"""
    This program is used to find the sum of the even-valued terms in a
    Fibonacci sequence. Recursive approach is used to compute the Fibonacci
    sequence.

    :copyright: (c) 2014 by Moataz Elmasry
"""

def fib(fib_limit):
    """Finds the sum of even numbers in a Fibonacci sequence up to limit.

    Args:
        fib_limit: upper-bound for even Fib numbers to sum.

    Returns:
        sum of even numbers in a Fibonacci sequence up to limit.
    """

# Prompt user for limit
fib_limit = int(input("Enter the value of the limit:\n"))

print("\nThe answer is:\n", fib(fib_limit))
