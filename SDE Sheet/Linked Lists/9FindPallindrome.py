from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the LinkedListNode class:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    nex = None

    while head:
        nex = head.next
        head.next = prev
        prev = head
        head = nex

    return prev


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    fast, slow = head, head

    # Find the middle point of the linked list
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half of the linked list
    slow.next = reverse(slow.next)
    slow = slow.next

    fast = head

    # Compare the first half with the reversed second half
    while slow:
        if slow.data != fast.data:
            return False
        slow, fast = slow.next, fast.next

    return True


def createLinkedList(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    return head


# Test Cases
# Test Case 1
arr1 = [5, 4, 3, 4, 5]
head1 = createLinkedList(arr1)
print(isPalindrome(head1))  # Output: True

# Test Case 2
arr2 = [1, 2, 3, 4, 5]
head2 = createLinkedList(arr2)
print(isPalindrome(head2))  # Output: False

# Test Case 3
arr3 = [1]
head3 = createLinkedList(arr3)
print(isPalindrome(head3))  # Output: True

# Test Case 4
arr4 = []
head4 = createLinkedList(arr4)
print(isPalindrome(head4))  # Output: True

# Test Case 5
arr5 = [1, 2, 1]
head5 = createLinkedList(arr5)
print(isPalindrome(head5))  # Output: True
