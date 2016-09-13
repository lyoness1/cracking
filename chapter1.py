# 1.1: Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?
# Runtime: O(n) to check each char in string
# Space: O(1) for 256 bitarray as an int "tracker"
# Edge cases: non ascii characters? 
def is_unique(string):
    """Returns a boolean indicating unique character content

        >>> is_unique("Helol, how are you?")
        False

        >>> is_unique("abcdeABCDE123")
        True

    """

    tracker = 0

    for char in string:
        # check if bits representing char have been flagged as true
        # bit array is 256 bits wide, representing ord(char) of ASCII chars
        # (1 << ord(char)) shifts the "true" bit over "ord(char)" times 
        if tracker & (1 << ord(char)):
            return False
        # flag bit tracking char as true
        # the |= retains original tracker value & adds the new ord(char) flag
        tracker |= (1 << ord(char))

    return True


# 1.2
# Runtime: O(n)
# Space: O(n) for new output string
# Edge cases: is not in place, as strings are immutable
def reverse_string(string):
    """Reverses a C-style string (includes null char)

        >>> reverse_string('abced')
        'decba'

        >>> reverse_string('Hello, how are you?')
        '?uoy era woh ,olleH'

    """

    output = ""
    for i in range(len(string)-1, -1, -1):
        output += string[i]
    return output


# 1.3
# Runtime: O(n)
# Space: O(n) for output string, O(1) for bitarray 255 
# Edge cases: non ascii chars
def remove_dupes(string):
    """Removes duplicate entries in string w/o additional buffer

        >>> remove_dupes('Hello, how are you?')
        'Helo, hwaryu?'

        >>> remove_dupes('Allison')
        'Alison'

    """

    tracker = 0
    output = ""

    for char in string:
        if not (tracker & (1 << ord(char))):
            output += char
        tracker |= (1 << ord(char))

    return output


# 1.4
# Runtime: O(n+m) to check each char
# Space: O(n+m) to make lower, O(1) if A != a
# Edge cases: capital vs. lower (anagrams or not?)
def are_anagrams(str1, str2):
    """Returns boolean indicating if str1 and str2 are are_anagrams

        >>> are_anagrams('abcde', 'ebcad')
        True

        >>> are_anagrams("AabBcD", "bbaacd")
        True

        >>> are_anagrams("abc", "def")
        False

    """
    # to all lower case, creates O(n+m) extra space for new strings, 
    # but allows a == A
    str1 = str1.lower()
    str2 = str2.lower()

    tracker1 = 0
    for char in str1:
        tracker1 |= (1 << ord(char))

    tracker2 = 0
    for char in str2:
        tracker2 |= (1 << ord(char))

    return tracker1 == tracker2


# 1.5
# Runtime: O(n)
# Space: O(n) for additional output string
# Edge cases: 
def change_spaces(phrase):
    """Replaces spaces in phrase with '%20'

        >>> change_spaces('Hello, how are you?')
        'Hello,%20how%20are%20you?'

    """

    output = ""
    for char in phrase:
        if char == " ":
            output += r'%20'
        else:
            output += char

    return output


# 1.6
# Runtime: O(n^2) to hit each element of matrix
# Space: O(1) when done in place
# Edge cases: 
def rotate_90(matrix):
    """Rotates NxN matrix of 4 byte pixels 90 degrees in place

        >>> rotate_90([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]])
        [[41, 31, 21, 11], [42, 32, 22, 12], [43, 33, 23, 13], [44, 34, 24, 14]]

    """
    # for doctest
    N = len(matrix)

    # there are N/2 layers (outside --> inside) to rotate
    for layer in range(N/2):
        # for each layer, make four shifts, using a tmp var for in place shift
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            tmp = matrix[first][i]
            # left --> top
            matrix[first][i] = matrix[last-offset][first]
            # bottom --> left
            matrix[last-offset][first] = matrix[last][last-offset]
            # right --> bottom
            matrix[last][last-offset] = matrix[i][last]
            # top --> right
            matrix[i][last] = tmp

    return matrix


# 1.7
# Runtime: O(nm) to iterate over every cell
# Space: O(n) worst case to store all rows/cols that need to zero out
# Edge cases: 
def set_zeros(matrix):
    """Nullifies rows and cols of any zero entry in matrix

    >>> set_zeros([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
    [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    """

    N = len(matrix)
    zero_rows = []
    zero_cols = []

    for row in xrange(N):
        for col in xrange(N):
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)

    for row in zero_rows:
        for i in range(N):
            matrix[row][i] = 0

    for col in zero_cols:
        for j in range(N):
            matrix[j][col] = 0

    return matrix


# 1.8
# Runtime:
# Space:
# Edge cases: already shifted
def is_substring(sub, string):
    """Returns boolean if sub is substring of string

        >>> is_substring("was", "I was here")
        True

        >>> is_substring("son", "Allison")
        True

        >>> is_substring("abc", "def")
        False

    """

    return sub in string

def is_rotation(s1, s2):
    """Checks if s1 is a rotation of s2

        >>> is_rotation("erbottlewat", "waterbottle")
        True

        >>> is_rotation("erb", "waterbottle")
        False

        >>> is_rotation("waterbottle", "waterbottle")
        True

    """

    if len(s1) != len(s2):
        return False

    return is_substring(s2, s1 + s1)
















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
