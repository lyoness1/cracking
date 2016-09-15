# TREES AND GRAPHS

# 4.1 Write a method to check for balance - no leafs differ by more than depth 1
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
class GraphNode(object):
    def __init__(self, value=None, adjacent=None):
        self.value = value
        self.adjacent = [] or adjacent

    def is_route(self, other):
        # """
        #     >>> n1 = DirectedGraph(1)
        #     >>> n2 = DirectedGraph(2)
        #     >>> n3 = DirectedGraph(3)
        #     >>> n4 = DirectedGraph(4)
        #     >>> n5 = DirectedGraph(5)
        #     >>> n6 = DirectedGraph(6)

        #     >>> n1.adjacent.append(n2)
        #     >>> n2.adjacent.append(n3)
        #     >>> n2.adjacent.append(n4)
        #     >>> n4.adjacent.append(n5)
        #     >>> n4.adjacent.append(n1)

        #     >>> n1.is_route(n5)
        #     True
        #     >>> n5.is_route(n1)
        #     False
        #     >>> n1.is_route(n6)
        #     False

        # """

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



# 4.4 Given a BST, write a fn that creates a LL of nodes at each depth
class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        ret = str(self.value)
        if self.next:
            ret += "-->" + self.next.__str__()
        else:
            ret += "-->None"
        return ret

class LL:
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = head or tail

    def add_node(self, node):
        self.tail.next = node
        self.tail = node

    

class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

    def make_ll_from_depth(self):
        """
            >>> bst = BSTNode(50, BSTNode(30, BSTNode(20, BSTNode(15), BSTNode(25)), BSTNode(40, BSTNode(35), BSTNode(45))), BSTNode(70, BSTNode(60, BSTNode(55), BSTNode(65)), BSTNode(80, BSTNode(75), BSTNode(85))))
            >>> bst.make_ll_from_depth()
            50-->None
            30-->70-->None
            20-->40-->60-->80-->None
            15-->25-->35-->45-->55-->65-->75-->85-->None

        """
        # 'global' variable to store lists by depth
        self.levels = {}

        def recurser(self, levels, depth=0):
            # add/update list at appropriate level
            if depth not in levels:
                levels[depth] = LL(LLNode(self))
            else:
                curr_ll = levels[depth]
                curr_ll.add_node(LLNode(self))
            # recurse downward
            if self.left:
                recurser(self.left, levels, depth+1)
            if self.right:
                recurser(self.right, levels, depth+1)
            # if leaf, return up callstack
            return 

        # start recurser with root
        recurser(self, self.levels)

        # print lists
        for lst in self.levels.values():
            print lst.head


# 4.5 Find 'next' node (in order) of a given node in BST w/ link to parent
class BSTNd:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return "<Node %s>" % self.value

    def __str__(self, depth=0):
        ret = ""
        if self.right != None:
            ret += self.right.__str__(depth + 1)
        ret += "\n" + ("    "*depth) + str(self.value)
        if self.left != None:
            ret += self.left.__str__(depth + 1)
        return ret

    def find_next(self):
        """
            >>> fifty = BSTNd(50)
            >>> thirty = BSTNd(30, fifty)
            >>> seventy = BSTNd(70, fifty)
            >>> twenty = BSTNd(20, thirty)
            >>> forty = BSTNd(40, thirty)
            >>> sixty = BSTNd(60, seventy)
            >>> eighty = BSTNd(80, seventy)
            >>> fifty.left = thirty
            >>> fifty.right = seventy
            >>> thirty.left = twenty
            >>> thirty.right = forty
            >>> seventy.left = sixty
            >>> seventy.right = eighty
            >>> thirty.find_next()
            40
            >>> twenty.find_next()
            30
            >>> fifty.find_next()
            60

        """
        def find_left_most_child(self):
            if not self.left:
                return self.value
            return find_left_most_child(self.left)

        # if no right children, return parent
        if not self.right:
            return self.parent.value
        # find left most child of self's right branch
        return find_left_most_child(self.right)

        # NOTE: doesn't account for starting w/ largest value in tree


# 4.6 Write a fn to find first common anscestor of two nodes in binary tree
def contain(root, node):
    if not root or not node:
        return False
    if root.value == node:
        return True
    return contain(root.left, node) or contain(root.right, node)

def find_first_comm_anscestor(root, a_value, b_value):
    """
        >>> bst = BSTNode(50, BSTNode(30, BSTNode(20, BSTNode(15), BSTNode(25)), BSTNode(40, BSTNode(35), BSTNode(45))), BSTNode(70, BSTNode(60, BSTNode(55), BSTNode(65)), BSTNode(80, BSTNode(75), BSTNode(85))))
        >>> find_first_comm_anscestor(bst, 35, 45)
        40
        >>> find_first_comm_anscestor(bst, 55, 85)
        70
        >>> find_first_comm_anscestor(bst, 45, 40)
        40
    """

    # base case: either a or b are not in the tree
    if not (contain(root, a_value) or contain(root, b_value)):
        return None
    # base cases for returning root:
    elif (# root is a, check below for b
           (root.value == a_value and (contain(root.left, b_value) or contain(root.right, b_value))) or
           # root is b, check below for a
           (root.value == b_value and (contain(root.left, a_value) or contain(root.right, a_value))) or
           # a and b are in opposite branches
           (contain(root.right, a_value) and contain(root.left, b_value)) or
           (contain(root.right, b_value) and contain(root.left, a_value))
        ):
        return root.value
    # progress: both a and b are left
    elif contain(root.left, a_value) and contain(root.left, b_value):
        return find_first_comm_anscestor(root.left, a_value, b_value)
    # progress: both a and b are right
    return find_first_comm_anscestor(root.right, a_value, b_value)














if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\n ALL TESTS PASSED!! \n\n"

        