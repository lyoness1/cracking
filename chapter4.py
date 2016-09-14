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

# Generic Tree Structure
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
# route be- tween two nodes. 
"""
    >>> 

"""
class DirectedGraphNode(object):
    def __init__(self)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\n ALL TESTS PASSED!! \n\n"

        