class LinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList [ " + "->".join(nodestore) + " ]"
        return "LinkedList []"

    def add_node(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_node(self, value):
        curr = self.head
        # if head is value to remove, reset head to head.next
        if curr.value == value:
            self.head = curr.next
        # progress until finding value, update previous pointer to next pointer
        while curr:
            prev = curr
            curr = prev.next
            if curr and curr.value == value:
                prev.next = curr.next
        if curr == None:
            raise Exception("Value does not exist in list")



# 2.1 Remove duplicate from an unsorted linked list
# What if no additional buffer is allowed? 
# Runtime: o(n)
# Space: o(n)
# Edge cases: 
def remove_dupes(LL):
    """Remove duplicated from an unsorted linked list

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('C')
        >>> d = LinkedListNode('B')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> lst = LinkedList(a)
        >>> remove_dupes(lst)
        >>> print lst
        LinkedList [ A->B->C ]

    """

    seen = set(LL.head.value)

    curr = LL.head

    while curr:
        prev = curr
        curr = prev.next
        if curr and curr.value in seen:
            prev.next = curr.next
        elif curr:
            seen.add(curr.value)

# 2.1 - Without additional buffer
# Runtime: O(n^2)
# Space: O(1)
def remove_dupes_wo_buffer(LL):
    """Remove duplicated from an unsorted linked list

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('C')
        >>> d = LinkedListNode('B')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> lst = LinkedList(a)
        >>> remove_dupes_wo_buffer(lst)
        >>> print lst
        LinkedList [ A->B->C ]

    """

    runner1 = LL.head
    
    while runner1:
        runner2 = runner1
        while runner2:
            curr = runner2
            runner2 = runner2.next
            if runner2 and (runner2.value == runner1.value):
                curr.next = runner2.next
        runner1 = runner1.next


# 2.2 Return the n'th to last node in a SLL
# Runtime: O(n)
# Space: O(1)
def find_nth_to_last(LL, n):
    """Returns the nth to last node in SLL

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('C')
        >>> d = LinkedListNode('D')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> lst = LinkedList(a)
        >>> find_nth_to_last(lst, 2)
        'C'

    """
    # send first runner ahead n steps
    runner1 = LL.head
    steps = 1
    while steps <= n:
        if not runner1:
            raise Exception("List is not long enough")
        runner1 = runner1.next
        steps += 1

    # start runner2 n steps behind runner 1
    runner2 = LL.head
    while runner1:
        runner1 = runner1.next
        runner2 = runner2.next

    return runner2.value


# 2.3 Delete a node with only a reference to the value of the node
# Runtime: O(n)
# Space: O(1)
def delete_node(LL, value):
    """Deletes a node from a SLL given only the value of the node

        >>> a = LinkedListNode('A')
        >>> b = LinkedListNode('B')
        >>> c = LinkedListNode('C')
        >>> d = LinkedListNode('D')
        >>> a.next = b
        >>> b.next = c
        >>> c.next = d
        >>> lst = LinkedList(a)
        >>> delete_node(lst, 'C')
        >>> print lst
        LinkedList [ A->B->D ]

    """

    curr = LL.head

    while curr.next: 
        prev = curr
        curr = curr.next
        if curr.value == value:
            prev.next = curr.next


# 2.4 Add two numbers stored as LL, head is one's place
# Runtime: O(n) where n is the number of digits in the longer input number
# Space: O(n) for output
def add_two_nums(LL1, LL2):
    """Returns a LL that is the sum of two LL's

        >>> LL1 = LinkedList(LinkedListNode(3, LinkedListNode(1, LinkedListNode(5))))
        >>> LL2 = LinkedList(LinkedListNode(6, LinkedListNode(9, LinkedListNode(2))))
        >>> add_two_nums(LL1, LL2)
        LinkedList [ 9->0->8 ]

    """

    a = LL1.head
    b = LL2.head

    carryover = 0

    output = LinkedList()

    while a and b:
        digit = a.value + b.value + carryover
        carryover, digit = divmod(digit, 10)
        output.add_node(digit)
        a = a.next
        b = b.next

    if b and (not a):
        while b:
            digit = b.value + carryover
            carryover, digit = divmod(digit, 10)
            output.add_node(digit)
            b = b.next

    if a and (not b):
        while a:
            digit = a.value + carryover
            carryover, digit = divmod(digit, 10)
            output.add_node(digit)
            a = a.next

    print output


# 2.5








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
