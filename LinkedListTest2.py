"""
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list and next line contains the linked list elements.

Output:
For each testcase, there will be a single line of output which contains the linked list with every k group elements reversed.

Example:
Input:
1
8
1 2 2 4 5 6 7 8
4

Output:
4 2 2 1 8 7 6 5

Explanation:
Testcase 2: Since, k = 4. So, we have to reverse everty group of two elements. Modified linked list is as 4, 2, 2, 1, 8, 7, 6, 5.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverseK(self, k):
        # counter = 1
        prev = None
        curr = self.head
        while curr is not None:
            for i in range(k):
                if curr is None:
                    break
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                # counter += 1
            prev = self.head
            self.head = curr
        self.head = prev

llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("input")
llist.printList()
llist.reverseK(3)
print("reverse")
llist.printList()