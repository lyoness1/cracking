# TREES AND GRAPHS


# Generic Tree Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        node = Node(value)
        self.children.append(node)


# Write a fn to determine if a tree is balanced
class BalancedTree:
    def __init__(self, root):
        self.root = root

    def check_for_balance(self):
        if not self.root:
            return True

        # depth first search using to_visit stack
        to_visit = [self.root]
        # dictionary to track depth counts for each leaf
        depths = {}
        # initialize depth=0 for root
        depth = 0

        while to_visit:
            node = to_visit.pop()
            # base case: found leaf, update depths dict
            if not node.children:
                if depth in depths:
                    depths[depth] += 1
                else: 
                    depths[depth] = 1
            # progress: add children to to_visit stack
            else: 
                to_visit.extend(node.children)

        # analyze tree depths
        keys = depths.keys()
        if len(keys) < 1 or abs(keys[1] - keys[0]) < 2:
            return True
        else: 
            return False





        