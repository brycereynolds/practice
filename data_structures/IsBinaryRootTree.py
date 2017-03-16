class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, val):
        if val is self.data:
            return True

        if val < self.data:
            if self.left != None:
                return self.left
            else:
                return False

        if val > self.data:
            if self.right != None:
                return self.right
            else:
                return False

    def printTree(self):
        if self.left != None:
            self.left.printTree()

        print(self.data)

        if self.right != None:
            self.right.printTree()

# 2
# 1 2 2 4 5 6 7
# No

a = Node(2)
a.insert(1)
a.insert(2)
a.insert(2)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.printTree()



""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root, lower=None, upper=None):
    if root is None or root.data is None:
        return False

    if lower != None and root.data < lower:
        return False
    
    if upper != None and root.data > upper:
        return False
    
    if root.left != None:
        if root.left.data >= root.data or check_binary_search_tree_(root.left, lower, root.data - 1) is False:
            return False

    if root.right != None:
        if root.right.data <= root.data or check_binary_search_tree_(root.right, root.data + 1, upper) is False:
            return False

    return True

