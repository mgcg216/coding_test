

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class binarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, root, node):
        if self.root is None:
            root = Node(val)
        else:
            root.val >