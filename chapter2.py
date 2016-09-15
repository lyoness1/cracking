# 2.1
# Runtime: 
# Space:
# Edge cases: 
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_duplicates_time(head):
    """Removes duplicates from SLL

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('A')
        >>> d = LinkedListNode('D')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> remove_duplicates_time(a)
        >>> print b.next.value
        D

    """
    seen = set(head.value)

    curr = head

    while curr.next:
        if curr.next.value in seen:
            curr.next = curr.next.next
        curr = curr.next

    
def remove_duplicates_space(head):
    """Removes duplicates from SLL

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('A')
        >>> d = LinkedListNode('D')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> remove_duplicates_space(a)
        >>> print b.next.value
        D

    """

    








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
