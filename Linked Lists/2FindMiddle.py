# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        # Initialize two pointers, slow and fast, both pointing to the head
        slow = head
        fast = head

        # Move the fast pointer by two nodes and the slow pointer by one node
        # When the fast pointer reaches the end of the list, the slow pointer will be at the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Return the slow pointer, which is the middle node
        return slow


# Test Cases

# Test Case 1:
# A single node, the middle node is the head node itself.
head = ListNode(1)
solution = Solution()
result = solution.middleNode(head)
print(result.val)  # Output: 1

# Test Case 2:
# A linked list with odd number of nodes.
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
result = solution.middleNode(head)
print(result.val)  # Output: 3

# Test Case 3:
# A linked list with even number of nodes.
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
solution = Solution()
result = solution.middleNode(head)
print(result.val)  # Output: 4
