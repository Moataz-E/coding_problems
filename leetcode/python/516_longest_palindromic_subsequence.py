"""
Given a string s, find the longest palindromic subsequence's length in s. You
may assume that the maximum length of s is 1000.

Note that an example of a subsequence for "bbbab" is "bbbb", with the "a"
skipped over. It is technically a powerset of the letters in the string with
original order intact.

Example 1: "bbbab" -> 4
Example 2: "cbbd" -> 2
"""

class LongestPalindromeSubseq:

    def longestPalindromeSubseq(self, s):
        """find the longest palindromic subsequence's length in string.

        Args:
            s: string

        Returns:
            Integer for length of longest palindromic sequence in string.
        """
        s_powerset = self.powerset(s)
        print(s_powerset)
        max_palindrome = 0
        for s in s_powerset:
            if s == self.reverse(s):
                max_palindrome = max(max_palindrome, len(s))
        print(max_palindrome)
        return max_palindrome

    def reverse(self, s):
        """Reverse string"""
        str_list = list(s)
        lm = 0
        rm = len(str_list) - 1
        while lm < rm:
            str_list[lm], str_list[rm] = str_list[rm], str_list[lm]
            lm += 1
            rm -= 1
        return ''.join(str_list)

    def powerset(self, s):
        """Returns powerset of a string.

        Args:
            s: string

        Returns:
            List containing powerset of string.
        """
        ss = []
        for cs in range(1, len(s)+1):
            for i in range(len(s)+1-cs):
                for j in range(i+1, i+1+len(s)-cs+1):
                    e = s[i] + s[j:j+cs-1]
                    ss.append(e)
        return set(ss)

lps = LongestPalindromeSubseq()

A = "ab"
assert(len(lps.powerset(A)) == 3)
assert(lps.reverse(A) == "ba")

B = "abc"
assert(len(lps.powerset(B)) == 7)
assert(lps.reverse(B) == "cba")

C = "abcd"
assert(len(lps.powerset(C)) == 14)
assert(lps.reverse(C) == "dcba")
lps.powerset("aaa")
