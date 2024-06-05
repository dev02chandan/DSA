# Another Approach (Striver)

class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # If k is 0 or head is None, no rotation needed
    if k == 0 or head is None:
        return head

    slow = head
    count = 1

    # Get the length of the linked list
    while slow.next is not None:
        slow = slow.next
        count += 1

    # If k is greater than or equal to the count, take modulus to get effective rotation
    if k >= count:
        k = k % count

    # Make the linked list circular by connecting the last node with the head
    slow.next = head

    # Move slow to the (count - k)th node
    for i in range(count - k):
        slow = slow.next

    # Break the circular link to make slow the new tail of the rotated list
    nex = slow.next
    slow.next = None

    return nex

# Approach:
# 1. If k is 0 or the head is None, there is nothing to rotate, so return the head as it is.
# 2. Traverse the linked list to find its length and keep track of the last node (slow) and the count.
# 3. If k is greater than or equal to the count, take the modulus of k with count to get the effective rotation.
# 4. Make the linked list circular by connecting the last node (slow) with the head.
# 5. Move slow to the (count - k)th node, which will be the new last node after rotation.
# 6. Break the circular link by setting slow.next to None, making it the new tail of the rotated linked list.
# 7. Return the next node after slow as the new head of the rotated linked list.
# Time complexity: O(N) where N is the length of the linked list.
# Space complexity: O(1)


# Testcases
# 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 2
rotated_head = rotate(head, k)
print(rotated_head.data, end=" -> ")  # Output: 4 -> 5 -> 1 -> 2 -> 3 -> None
print(rotated_head.next.data, end=" -> ")
print(rotated_head.next.next.data, end=" -> ")
print(rotated_head.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.next)

# 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 0
rotated_head = rotate(head, k)
print(rotated_head.data, end=" -> ")  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
print(rotated_head.next.data, end=" -> ")
print(rotated_head.next.next.data, end=" -> ")
print(rotated_head.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.next)

# 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 8
rotated_head = rotate(head, k)
print(rotated_head.data, end=" -> ")  # Output: 3 -> 4 -> 5 -> 1 -> 2 -> None
print(rotated_head.next.data, end=" -> ")
print(rotated_head.next.next.data, end=" -> ")
print(rotated_head.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.data, end=" -> ")
print(rotated_head.next.next.next.next.next)

head = Node(1)  # 1 -> None
k = 3
rotated_head = rotate(head, k)
print(rotated_head.data, end=" -> ")  # Output: 1 -> None
print(rotated_head.next)

head = None  # None
k = 5
rotated_head = rotate(head, k)
print(rotated_head)  # Output: None
