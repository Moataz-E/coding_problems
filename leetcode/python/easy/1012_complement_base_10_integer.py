"""
Every non-negative integer N has a binary representation.  For example, 5 can
be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note
that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when
changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in
binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary
representation as a base-10 integer.
"""
class ComplementBaseTenInt(object):

    def flip(self, n):
        if n == '1':
            return '0'
        else:
            return '1'

    def bitwise_complement(self, N:int) -> int:
        """Finds binary complement of a number in base 10.

        Leetcode stats:
            Runtime: 36ms
            Memory Usage: 13.2MB

        Args:
            N: Integer whose complement we want to find.

        Returns:
            Integer form of the binary complement of integer N.
        """
        bin_fmt = bin(int(N))
        flipped = [self.flip(x) for x in list(bin_fmt)[2:]]
        return int(''.join(flipped), 2)

cbi = ComplementBaseTenInt()
assert(cbi.bitwise_complement(5) == 2)
assert(cbi.bitwise_complement(0) == 1)
