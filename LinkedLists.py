"""
Linked Lists Practice
"""
# Embedded references
# We have seen examples of attributes that refer to other objects, which we called embedded references. A common data structure,
#  the linked list, takes advatage of this feature. Linked list are made up of nodes, where each node contains a reference to the next node in
# the list. In addition, each node contains a unit of data called the cargo.
# A linked list is considered a recursive data structure because it has recursive definition.
# A linked list is either:
#   1. the empty list, represented by None, or
#   2. a node that contains a cargo object and a reference to a linked list
# Recursive data structures lend themselves to recursive methods.
class Node:
    def __init__(self, cargo=None, next=None, prev=None,):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.cargo)

def add(node):
    pass

def print_list(node):
    while node:
        print(node)
        node = node.next
    print


def print_backwards(node):
    if node is None:
        return
    head = node
    tail = node.next
    print_backwards(tail)
    print(head)

def reverse(node):
    if node is None:
        return
    head = node
    tail = node.next
    print_backwards(tail)
    head.next = None
    tail.next = head

def remove(node):
    pass

# node = Node("test")
# print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


node1.next = node2
node2.next = node3

print_list(node1)

print_backwards(node1)

reverse(node1)

print_list(node1)


