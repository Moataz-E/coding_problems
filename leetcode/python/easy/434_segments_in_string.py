"""
Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""

class SegmentsInString:

    def count_segments(self, s: str) -> int:
        """Counts number of segments in a string.

        Leetcode stats:
            Runtime: 48ms
            Memory Usage: 13.1MB

        Args:
            s: string containing words and whitespace

        Returns:
            Integer number of segments in string.
        """
        words = [x for x in s.split(' ') if x != '']
        return len(words)

sis = SegmentsInString()
assert(sis.count_segments("moataz elmasry") == 2)
assert(sis.count_segments("  ") == 0)
assert(sis.count_segments(" a sd wa") == 3)
