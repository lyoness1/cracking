# TREES AND GRAPHS

# 4.1 Write a method to check for balance - no leafs differ by more than depth 1
"""
    >>> unbalanced = Node('0', [Node('0_0', [Node('0_0_0', [Node("extra")]), Node('0_0_1')]), Node('0_1', [Node('0_1_0')]), Node('0_2')])
    >>> unbalanced.check_for_balance()
    False
    >>> balanced = Node('0', [Node('0_0', [Node('0_0_0'), Node('0_0_1')]), Node('0_1', [Node('0_1_0')]), Node('0_2')])
    >>> balanced.check_for_balance()
    True
    >>> Node().check_for_balance()
    True

"""

class Node(object):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

    def __str__(self, level=0):
        ret = '\t' * level + repr(self.value)
        for child in self.children:
            ret += '\n' + child.__str__(level+1)
        return ret

    def __repr__(self):
        return self.value

    def check_for_balance(self):
        return (self.get_max_depth() - self.get_min_depth() < 2)

    def get_min_depth(self):
        if not self.children:
            return 0
        return 1 + min(child.get_min_depth() for child in self.children)

    def get_max_depth(self):
        if not self.children: 
            return 0
        return 1 + max(child.get_max_depth() for child in self.children)  


# 4.2 Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes. 
"""
    >>> n1 = DirectedGraph(1)
    >>> n2 = DirectedGraph(2)
    >>> n3 = DirectedGraph(3)
    >>> n4 = DirectedGraph(4)
    >>> n5 = DirectedGraph(5)
    >>> n6 = DirectedGraph(6)

    >>> n1.adjacent.append(n2)
    >>> n2.adjacent.append(n3)
    >>> n2.adjacent.append(n4)
    >>> n4.adjacent.append(n5)
    >>> n4.adjacent.append(n1)

    >>> n1.is_route(n5)
    True
    >>> n5.is_route(n1)
    False
    >>> n1.is_route(n6)
    False

"""

class GraphNode(object):
    def __init__(self, value=None, adjacent=None):
        self.value = value
        self.adjacent = [] or adjacent

    def is_route(self, other):
        visited = set(self)
        while visited: 
            curr = visited.pop()
            if curr == other:
                return True
            if self.adjacent:
                    visited.add(self.adjacent - visited)
        return False


# 4.3 Given a sorted array, write a fn to create a binary tree of min height
# perfect binary tree: n = 2^(h+1) - 1
# n + 1 = 2^(h+1)
# lg(n + 1) = (h + 1) * lg(2) = h + 1
# h = lg(n + 1) - 1
def make_tree(arr):
    """Creates a tree of minimum height given a sorted array.

        >>> print make_tree([1, 2, 3, 4, 5, 6, 7, 8])
        <BLANKLINE>
                8
            7
                6
        5
                4
            3
                2
                    1
        >>> print make_tree(['a', 'b', 'c', 'd'])
        <BLANKLINE>
            d
        c
            b
                a
        
    """
    # base case: empty array, return None
    if not arr: 
        return None

    # base case: only one item, create leaf node with item
    if len(arr) == 1:
        return BinaryNode(arr[0])

    # progress: use center item to ensure min depth
    else:
        mid = len(arr) / 2
        return BinaryNode(
            arr[mid],                   # make node at center item
            make_tree(arr[:mid]),       # make left tree with left half
            make_tree(arr[mid+1:])      # make right tree with right half
        )
        

class BinaryNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, depth=0):
        ret = ""

        if self.right != None:
            ret += self.right.__str__(depth + 1)

        ret += "\n" + ("    "*depth) + str(self.value)

        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret














if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\n ALL TESTS PASSED!! \n\n"

        