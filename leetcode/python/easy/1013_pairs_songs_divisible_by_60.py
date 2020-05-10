"""
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60.  Formally, we want the number of indices i < j with
(time[i] + time[j]) % 60 == 0.
"""
from typing import List
from itertools import combinations
from collections import Counter

class SongPairsDivBy60(object):

    def pairs_divisible_by_60(self, time: List[int]) -> int:
        """Return number of pairs whose sum is divisible by 60.

        Leetcode stats:
            Runtime: Time Limit Exceeded
            Memory Usage: Time Limit Exceeded

        Args:
            time: list of integers where each represents the duration of a song.

        Returns:
            Number of pairs whose total duration is divisible by 60.
        """
        combs = combinations(list(range(len(time))), 2)
        count = sum([1 for i,j in combs if (time[i] + time[j]) % 60 == 0])
        return count

    def pairs_divisible_by_60_fast(self, time: List[int]) -> int:
        """Return number of pairs whose sum is divisible by 60.

        Leetcode stats:
            Runtime: 116ms
            Memory Usage: 15.5MB

        Args:
            time: list of integers where each represents the duration of a song.

        Returns:
            Number of pairs whose total duration is divisible by 60.
        """
        counter = Counter()
        count = 0
        for t in time:
            # Find out if we have encountered any number whose modulo 60 is
            # a number that adds up to 60 with the modulo 60 of this time t.
            # Add that number's count to our running count.
            count +=  counter[(60 - (t % 60)) % 60]
            counter[t % 60] += 1
        return count

sp = SongPairsDivBy60()
t = [30,20,150,100,40]
assert(sp.pairs_divisible_by_60(t) == 3)
assert(sp.pairs_divisible_by_60_fast(t) == 3)

t2 = [60,60,60]
assert(sp.pairs_divisible_by_60(t2) == 3)
assert(sp.pairs_divisible_by_60_fast(t2) == 3)
