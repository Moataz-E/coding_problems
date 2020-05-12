"""
You are given a sorted array consisting of only integers where every element 
appears exactly twice, except for one element which appears exactly once. Find 
this single element that appears only once.
"""

class ElementInArray(object):

    def single_non_duplicate(self, nums):
        """Finds single element in an array where every element is there twice.
        
        Args:
            nums: sorted List[int]

        Returns:
            int representing non-duplicate elemnt. 
        """
        last_element = nums[0]
        last_element_count = 1
        for i in nums[1:]:
            if i != last_element:
                if last_element_count == 1:
                    break
                last_element = i
                last_element_count = 1
            else:
                last_element_count += 1
        return last_element

eia = ElementInArray()
assert eia.single_non_duplicate([1,1,4,4,12,12,15,16,16,37,37]) == 15
assert eia.single_non_duplicate([4,8,8,10,10,13,13]) == 4