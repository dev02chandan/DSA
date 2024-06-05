# Python TC - 95.27% SC - 92.29% on coding ninjas

from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin

# Following is the linked list node structure:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to merge two sorted linked lists


def sortTwoLists(first, second):
    # Base cases
    if first is None and second is None:
        return None
    if first is None:
        return second
    if second is None:
        return first

    # Determining the smaller head node
    if first.data > second.data:
        ptr1 = second
        ptr2 = first
        first = None
        # Keeping first None - later to know I have to return second
    else:
        ptr1 = first
        ptr2 = second
        second = None

    dummy = None

    # Merging the two lists
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data <= ptr2.data:
            dummy = ptr1
            ptr1 = ptr1.next
        else:
            nexxt = ptr2.next
            dummy.next = ptr2
            dummy = dummy.next
            ptr2.next = ptr1
            ptr2 = nexxt

    # If ptr1 reaches the end of its list, append the remaining nodes of ptr2
    while ptr2 is not None:
        dummy.next = ptr2
        dummy = dummy.next
        ptr2 = ptr2.next

    # Return the merged list
    if first is None:
        return second
    else:
        return first


def ll(arr):
    # Create a linked list from an array
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        last.next = Node(data)
        last = last.next

    return head


def printll(head):
    # Print the linked list
    while head:
        print(head.data, end=' ')
        head = head.next
    print(-1)


t = int(sys.stdin.readline().strip())

for i in range(t):
    # Read inputs for two linked lists
    arr1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))

    # Create linked lists from the input arrays
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])

    # Merge and sort the linked lists
    l = sortTwoLists(l1, l2)

    # Print the merged and sorted linked list
    printll(l)
