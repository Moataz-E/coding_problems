"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.
"""

class LengthLastWord:

    def length_last_word(self, s: str) -> int:
        """Retrieves length of last word in string.

        Leetcode stats:
            Runtime: 40ms
            Memory Usage: 13.2MB

        Args:
            s: string containing words

        Returns:
            Integer representing length of last word in string.
        """
        words = [x for x in s.split(' ') if x != '']
        if len(words) < 1:
            return 0
        return len(words[-1])

llw = LengthLastWord()
assert(llw.length_last_word("moataz elmasry") == 7)
assert(llw.length_last_word("") == 0)
assert(llw.length_last_word("   ") == 0)
assert(llw.length_last_word("    a   ") == 1)
