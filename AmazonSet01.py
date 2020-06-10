"""
Online Coding Test (4 Problems, 2 hours) From Interviewstreet
All below problems had multiple test cases for which the code was validated against.
1. Code for converting floating point decimal number to binary numbers. If the number cannot be converted, state so.
2. Given an integer array A of size n. Given an integer k < n. Construct an array B, such that B[i] = min{A[i], A[i+1],
 A[i+2], A[i+3], ……., A[i+k]} Solve in time complexity better than O(nk). Hint: use min Heaps
 3. A singly liked list. Can have a loop. Detect it and find the size of list.
4. A singly link list and a number ‘K’, swap the Kth node from the start with the Kth node from the last. Check all the edge cases.
Sample Input: 1->2->3->4->5->6->7->8 and K = 3
Sample Output : 1->2->6->4->5->3->7->8

Sample Input: 1->2->3->4->5->6->7->8 and K = 10
Sample Output: print error “LIST IS OF LESSER SIZE”.

"""

def floatToBinary(num):
    out = ""
    while True:
        if num < 1:
            break
        out = out + str(num%2)
        num = num//2
    return out

print(floatToBinary(17))


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

def sizeNode(start, size=1):
    if start.next is not None:
        size = size + 1
        sizeNode(start.next, size)
    if start.next is None:
        print(size)

size = sizeNode(node1)
print(size)
    




