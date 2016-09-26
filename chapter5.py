# BIT MANIPULATION

""" 
5.1 
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write
a method to set all bits between i and j in N equal to M (e.g., M becomes a 
substring of N located at i and starting at j). 
EXAMPLE: 
Input: N = 10000000000, M = 10101, i = 2, j = 6 
Output: N = 10001010100 
"""

def make_bit_substring(N, M, i, j):
    """
        >>> make_bit_substring(10000000000, 10101, 2, 6)
        10001010100

    """











if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\n ALL TESTS PASSED!! \n\n"