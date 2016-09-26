# BIT MANIPULATION

""" 
5.1 
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write
a method to set all bits between i and j in N equal to M (e.g., M becomes a 
substring of N located at i and starting at j). 
"""
def make_bit_substring(N, M, i, j):
    """
        >>> make_bit_substring(10000000000, 10101, 2, 6)
        10001010100

    """

    N = str(N)
    M = str(M)

    return int(N[:len(N)-j-1] + str(M) + N[len(N)-i:])


def make_bit_substring_again(N, M, i, j):
    """Converting each step int --> bin --> str

        >>> make_bit_substring_again(10000010000, 10101, 2, 6)
        10001010100

    """

    # Binary string of 1's the length of N
    var = str(int('1' * len(str(N))))  # '11111111111'

    # Binary string of 1's the length of j
    shift_left = str(bin((1 << j) - 1))[2:]  # '111111'
    # All 1's from j left
    left = str(bin(int(var, 2) - int(shift_left, 2)))[2:]  # '11111000000'
    # All 1's from i right
    right = str(bin((1 << i) - 1))[2:]  # '11'

    # All 1's except for j to i
    mask = str(bin((int(left, 2) | int(right, 2))))[2:]  # '11111000011'

    # N with zeros where M will go
    n_mask = str(bin(int(str(N), 2) & int(mask, 2)))[2:]  # '1000000000'
    # M shifted i units left
    m_shift = str(bin(int(str(M), 2) << i))[2:]  # '1010100'

    # M inserted into N on top of zeros created from mask
    return int(bin(int(n_mask, 2) | int(m_shift, 2))[2:])  # ''


def make_bit_substring_third(N, M, i, j):
    """Converting each step int --> bin --> str

        >>> make_bit_substring_third(10000110010, 10101, 2, 6)
        10001010110

    """
    # int version of 1's the length of N
    var = int('1' * len(str(N)))  # 11111111111
    
    left = var - int('1' * j)  # 11111000000
    right = int(('1' * i))  # 11

    mask = left | right  # 11111000011

    n_and = int(str(N), 2) & int(str(mask), 2)  # 1026
    m_shift = (int(str(M), 2) << i)  # 84

    return int(str(bin(n_and | m_shift))[2:])














if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\n ALL TESTS PASSED!! \n\n"