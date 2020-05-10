"""
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length
"""
from typing import List


class MaxAbsExpr(object):
    """
    Main intuition is each of the indices in the two arrays can have one of
    the following contributions to the final result per the formula provided:

    1. arr1[i] + arr2[i] + i
    2. arr1[i] + arr2[i] - i
    3. arr1[i] - arr2[i] + i
    4. arr1[i] - arr2[i] - i

    We create these four compressed arrays and scan each of the arrays
    attempting to find the two pairs with the maximum absolute difference. We
    then find the maximum of the four maximums obtained from the compressed
    arrays.
    """

    def max_diff_comps(self, arr:List[int]) -> int:
        """Finds max difference in a compressed array."""
        min_val = float('inf')
        max_val = float('-inf')
        max_diff = 0
        for i in range(len(arr)):
            min_val = min(min_val, arr[i])
            max_val = max(max_val, arr[i])
            max_diff = max(
                max_diff,
                abs(arr[i] - min_val),
                abs(arr[i] - max_val)
            )
        return max_diff

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """Calculates maximum absolute value for expression.

        Leetcode stats:
            Runtime: 324ms
            Memory Usage: 24.1MB
        """
        # Create compressed arrays
        c1, c2, c3, c4 = [], [], [], []
        for i in range(len(arr1)):
            c1.append(arr1[i] + arr2[i] + i)
            c2.append(arr1[i] + arr2[i] - i)
            c3.append(arr1[i] - arr2[i] + i)
            c4.append(arr1[i] - arr2[i] - i)
        # Find maximum difference in each compressed array
        c1_diff = self.max_diff_comps(c1)
        c2_diff = self.max_diff_comps(c2)
        c3_diff = self.max_diff_comps(c3)
        c4_diff = self.max_diff_comps(c4)
        return max(c1_diff, c2_diff, c3_diff, c4_diff)


mae = MaxAbsExpr()
assert mae.maxAbsValExpr([1,2,3,4], [-1,4,5,6]) == 13
assert mae.maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]) == 20
print( mae.maxAbsValExpr([1,2,3,4], [-1,4,5,6]))
print( mae.maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]))
