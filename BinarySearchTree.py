"""
The following is definition of Binary Search Tree(BST) according to Wikipedia

Binary Search Tree, is a node-based binary tree data structure which has the following properties:
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
There must be no duplicate nodes.
"""

class Node:
    def __init__(self, key, left = None, right=None):
        self.val = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)



def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

class DNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def push(self, val):
        new_node = DNode(val)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next


def toLinkedList(root, llist):
    if root:
        toLinkedList(root.right, llist)
        llist.push(root.val)
        toLinkedList(root.left, llist)

def find(root, key):
    pass


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
inOrder(r)

# This code is contributed by Bhavya Jain

llist = LinkedList()
toLinkedList(r, llist)
llist.printList()