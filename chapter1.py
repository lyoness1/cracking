# 1.1: Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
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
    # to all lower case, creates O(n+m) extra space for new strings, but allows a == A
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
# Runtime:
# Space:
# Edge cases: 
def rotate_90(matrix):
    """Rotates NxN matrix of 4 byte pixels 90 degrees in place

        >>> rotate_90([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]])
        [[41, 31, 21, 11], [42, 32, 22, 12], [43, 33, 23, 13], [44, 34, 24, 14]]

    """
    # for doctest
    N = len(matrix)

    output = []
    # for each col, create a row from a column
    for col in range(N):
        new_row = []
        for row in range(N-1, -1, -1):
            new_row.append(matrix[row][col])
        output.append(new_row)

    return output







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
