"""
Given an array, rotate the array to the right by k steps, where k is
non-negative.
"""
from typing import List

class Rotate:

    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate a list to the right by k steps.

        Leetcode stats:
            Runtime: 52ms
            Memory Usage: 13.5MB

        Args:
            nums: list of ints.
            k: int representing degrees of rotation.
        """
        nums_cpy = nums[:]
        pivot = len(nums) - k
        for i in range(len(nums)):
            swap_loc = (i + pivot) % len(nums)
            nums[i] = nums_cpy[swap_loc]

    def reverse(self, nums, lm, rm):
        """Reverse list such that first element is last, etc."""
        while lm < rm:
            nums[lm], nums[rm] = nums[rm], nums[lm]
            lm += 1
            rm -= 1

    def rotate_no_extra_space(self, nums: List[int], k: int) -> None:
        """Rotates a list to the right by k steps using O(1) extra space.

        Leetcode stats:
            Runtime: 56ms
            Memory Usage: 13.3MB

        This solution reverses three core sublists as follows.
            1. All elements in the list.
            2. First k elements in the list.
            3. All elements from k onwards.
        Args:
            nums: list of ints
            k: int representing degrees of rotation
        """
        if (len(nums) < 2) or k == 0:
            return
        k = k % len(nums)

        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

rot = Rotate()

nums = [1,2,3,4,5,6]
rot.rotate(nums, 2)
assert(nums == [5,6,1,2,3,4])

nums = [1,2,3,4,5,6,7]
rot.rotate(nums, 3)
assert(nums == [5,6,7,1,2,3,4])

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
rot.rotate(nums, 17)
assert(nums == [10,11,12,13,1,2,3,4,5,6,7,8,9])

nums = [1,2,3,4,5,6]
rot.rotate_no_extra_space(nums, 2)
assert(nums == [5,6,1,2,3,4])

nums = [1,2,3,4,5,6,7]
rot.rotate_no_extra_space(nums, 3)
assert(nums == [5,6,7,1,2,3,4])

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
rot.rotate_no_extra_space(nums, 17)
assert(nums == [10,11,12,13,1,2,3,4,5,6,7,8,9])
