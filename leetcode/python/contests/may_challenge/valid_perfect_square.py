"""
Given a positive integer num, write a function which returns True if num is a 
perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""
import time

class PerfectSquare(object):

    def is_perfect_square_brute(self, num):
        """Brute force approach with early break.

        Not memory efficient.

        Args:
            num: int representing number to be checked.

        Returns:
            bool that is True if num is a perfect square.
        """
        if num < 2:
            return True
        for i in range(num):
            square = i*i
            if square == num:
                return True
            if square > num:
                break
        return False
        
    def is_perfect_square_bin_search(self, num):
        """Uses binary search to reduce search space.

        Args:
            num: int representing number to be checked.

        Returns:
            bool that is True if num is a perfect square.
        """
        if num < 2:
            return True
        lower_bound = 0
        upper_bound = num
        pivot = (upper_bound + lower_bound) // 2
        while lower_bound < upper_bound:
            print(pivot)
            square = pivot * pivot
            if square == num:
                return True
            elif square < num:
                lower_bound = pivot + 1
                pivot = (upper_bound + pivot) // 2
            else:
                upper_bound = pivot
                pivot = (lower_bound + pivot) // 2
        return False


# Test correctness and speed for square of 4658 which is 21696964.
ps = PerfectSquare()
start_t1 = time.time()
assert ps.is_perfect_square_brute(21696964) == True
brute_time = time.time() - start_t1
print("perfect_square_brute took {}s".format(brute_time))
start_t2 = time.time()
assert ps.is_perfect_square_bin_search(14) == True
binary_search_time = time.time() - start_t2
print("perfect_square_binary_search took {}s".format(binary_search_time))
print("binary search is {}X faster.".format(brute_time / binary_search_time))