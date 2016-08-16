# 1.1: Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
# Runtime:
# Space: 
# Edge cases: 
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
        if tracker & (1 << ord(char)):
            return False
        # flag bits tracking char as true
        tracker |= (1 << ord(char))

    return True







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
