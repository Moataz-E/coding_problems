"""
Given a string s, find the longest palindromic subsequence's length in s. You
may assume that the maximum length of s is 1000.

Note that an example of a subsequence for "bbbab" is "bbbb", with the "a"
skipped over. It is technically a powerset of the letters in the string with
original order intact.

Example 1: "bbbab" -> 4
Example 2: "cbbd" -> 2
"""
import itertools

class LongestPalindromeSubseq:

    def longest_palindrome_subseq(self, s: str) -> int:
        """Find the longest palindromic subsequence's length in string.

        We maintain a map of all the substrings of sring we've seen along
        with the length of the longest palindrome subsequence in that string.

        Not the fastest solution, but I believe the clearer and easiest to
        understand for a Dynamic Programmings solution.

        Args:
            s: str, for which we want to find longest palindrome subserquence.

        Returns:
            int, for length of longest palindromic sequence in string.
        """
        if not s: return 0
        seen = {}; max_palindrome = 0
        substrings = self.substrings(s)
        for ss in substrings:
            if ss in seen: continue
            s_len = len(ss); palindrome_len = 0
            if s_len < 1:
                palindrome_len = 0
            elif s_len < 2:
                palindrome_len = 1
            else:
                # If first and last letter in the string are the same
                if ss[0] == ss[-1]:
                    if s_len < 3:
                        palindrome_len = 2
                    else:
                        substring = ss[1:-1]
                        palindrome_len = 2 + seen[substring]
                # Otherwise, find the largest palindrome length from substrings
                # if we were to remove the first letter or the last letter
                else:
                    palindrome_len = max(seen[ss[1:]], seen[ss[:-1]])
            seen[ss] = palindrome_len
            max_palindrome = max(max_palindrome, palindrome_len)
        return max_palindrome

    def substrings(self, s: str):
        """Return all contiguous substrings of a string.
        
        Args:
            s: str, for which we want to find all substrings

        Returns:
            str generator, containing contiguous substrings of string sorted by
            length of substring.
        """
        s_len = len(s)
        sort_key = lambda x: int(x[1]) - int(x[0])
        for x,y in sorted(itertools.combinations(range(s_len+1), r=2), 
                          key=sort_key):
            yield s[x:y]


lps = LongestPalindromeSubseq()

A = "ab"
assert(len(list(lps.substrings(A))) == 3)

B = "abc"
assert(len(list(lps.substrings(B))) == 6)

C = "abcd"
assert(len(list(lps.substrings(C))) == 10)

E = "bbbab"
assert(lps.longest_palindrome_subseq(E) == 4)

F = "cbbd"
assert(lps.longest_palindrome_subseq(F) == 2)