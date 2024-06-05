from math import *
from collections import *
from sys import *
from os import *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedList(head):
    # Initialize a dummy node as the new head of the reversed linked list
    dummy = None

    # Traverse the original linked list
    while head is not None:
        # Store the next node in a temporary variable
        nextt = head.next

        # Reverse the link by pointing the current node's next to the previous node
        head.next = dummy

        # Move the dummy node to the current node
        dummy = head

        # Move to the next node in the original linked list
        head = nextt

    # Return the new head of the reversed linked list
    return dummy


# Test Cases
# Test Case 1: Empty linked list
# Expected Output: None
head1 = None
reversed_head1 = reverseLinkedList(head1)
print(reversed_head1)  # None

# Test Case 2: Linked list with a single node
# Expected Output: Node with data=1 and next=None
head2 = Node(1)
reversed_head2 = reverseLinkedList(head2)
print(reversed_head2.data)  # 1
print(reversed_head2.next)  # None

# Test Case 3: Linked list with multiple nodes
# Expected Output: Reversed linked list: 3 -> 2 -> 1 -> None
head3 = Node(1)
head3.next = Node(2)
head3.next.next = Node(3)
reversed_head3 = reverseLinkedList(head3)
current = reversed_head3
while current is not None:
    print(current.data)
    current = current.next
