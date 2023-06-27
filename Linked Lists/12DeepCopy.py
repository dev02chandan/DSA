class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def cloneRandomList(head):
    if not head:
        return head

    dummy = head

    while (dummy != None):
        new = LinkedListNode(dummy.data)
        nex = dummy.next
        dummy.next = new
        new.next = nex
        dummy = dummy.next.next

    dummy = head

    while (dummy != None):
        if dummy.random:
            dummy.next.random = dummy.random.next
        else:
            dummy.next.random = None
        dummy = dummy.next
        nex = dummy.next
        if dummy.next == None or dummy.next.next == None:
            break
        dummy.next = dummy.next.next
        dummy = nex

    return head.next

# Approach:
# 1. Traverse the original list and insert cloned nodes into the original list.
# 2. Update random pointers of the cloned nodes based on the random pointers of the original nodes.
# 3. Separate the cloned list from the original list by restoring the next pointers of the original list and the cloned list.
# 4. Return the head of the cloned list.
# Time complexity: O(N) where N is the length of the list.
# Space complexity: O(1)


# Test case 1
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.random = head.next.next
head.next.random = head
cloned_head = cloneRandomList(head)
# The original list: 1 -> 2 -> 3 (random pointer from 1 to 3, and from 2 to 1)
# The cloned list: 1' -> 2' -> 3' (random pointer from 1' to 3', and from 2' to 1')
# The cloned list should be: 1' -> 2' -> 3'
print(cloned_head.data)  # Output: 1
print(cloned_head.random.data)  # Output: 3
print(cloned_head.next.data)  # Output: 2
print(cloned_head.next.random.data)  # Output: 1
print(cloned_head.next.next.data)  # Output: 3
print(cloned_head.next.next.random)  # Output: None

# Test case 2
head = None
cloned_head = cloneRandomList(head)
# The original list is empty, so the cloned list should also be empty
print(cloned_head)  # Output: None
