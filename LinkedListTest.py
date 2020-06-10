

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

    def pull(self, val):
        temp = self.head
        while True:
            if temp.next is None:
                break
            temp = temp.next
        new_node = Node(val)
        temp.next = new_node

    # def reverse(self, node=head):
    #     if self.head.next is not None:
    #         self.head = node
    #         return
    #     self.reverse(node.next)
    #     temp = node.next
    #     temp.next = node
    #     node.next = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def find(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            node = node.next
        return False

    def remove(self, val):
        prev = None
        node = self.head
        while node:
            if node.val == val:
                if prev:
                    prev = node.next
                else:
                    node = node.next
                return True
        return False


    def printList(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next


# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.pull(12)

print("Given Linked List")
llist.printList()
llist.reverse()
print("Reversed Linked List")
llist.printList()

print(llist.find(4))
llist.remove(4)
print("Given Linked List after removing 4")
llist.printList()