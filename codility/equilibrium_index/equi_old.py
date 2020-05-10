#Find middle point of array.
#Find sum of lower part of array and sum of higher part of array.
#Conditions:
#    if sum to left < sum to right, then new midpoint is current midpoint
#    +(array.length - 1 )  / 2
#    if sum to left > sum to right, then new midpoint is current midpoint / 2
#    else point is equilibrium
from math import trunc


def sum_subarray(A, m, array_length):
    """Returns a list containing the sum of each the right and left subarrays.

    """

    left_subarray = A[0:m]
    right_subarray = A[m+1:(array_length - 1)]

    return [sum(left_subarray), sum(right_subarray)]


def left_or_right(A, m, array_length):
    """Check which subarray has a larger sum

    For an array A with midpoint m, if sum of all numbers in left array is 
    larger than numbers in right array, return -1. If the opposite, return +1.
    Returns 0 if left and right subarrays are equal

    """

    subarrays_sum = sum_subarray(A, m, array_length)

    if subarrays_sum[0] > subarrays_sum[1]:
        return -1
    elif subarrays_sum[0] < subarrays_sum[1]:
        return 1
    else:
        return 0
    

def solution(A):
    """Finds the equilibrium index of a list of integers.

    Given a zero-indexed array A consisting of N integers, returns any of
    its equilibrium indices. The function should return -1 if no
    equilibrium index exists.

    """

    array_length = len(A)

    midpoint = trunc( (array_length - 1) / 2 )

    leftOrRight = left_or_right(A, midpoint, array_length)

    while (leftOrRight != 0):
        if leftOrRight == -1:
            midpoint = trunc( (midpoint / 2) )

            leftOrRight = left_or_right(A, midpoint, array_length)

        elif leftOrRight == 1:
            midpoint = trunc( (midpoint + (array_length - 1)) / 2 )
            leftOrRight = left_or_right(A, midpoint, array_length)

        else:
            return -1
    return midpoint


A = [-7,1,5,2,-4,3,0]
print( solution(A) )





