'''
Approach:

First, we calculate the length of the linked list using the length() function. This helps us determine the effective rotation position if k is greater than the length of the linked list.
If k is greater than the length, we use the modulus operator to reduce it to an equivalent smaller value.
If k is 0 or the linked list is empty, we return the head as it is.
Next, we find the position at which we need to rotate the linked list. This position is calculated as count - k, where count is the length of the linked list.
We iterate through the linked list to find the new head node by moving rotate_pos positions from the current head.
We update the connections to rotate the linked list. We set the next pointer of the last node to the current head, and the next pointer of the node before the new head to None.
Finally, we return the new head node of the rotated linked list.
'''


class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def print_linked_list(head):
    """
    Print the elements of a linked list.

    Args:
        head: Head node of the linked list.

    """
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


def length(head):
    """
    Calculate the length of the linked list.

    Args:
        head: Head node of the linked list.

    Returns:
        The length of the linked list.
    """
    count = 0
    while head and head.next:
        head = head.next
        count += 1

    return count + 1


def rotate(head: Node, k: int) -> Node:
    """
    Rotate a linked list by k positions.

    Args:
        head: Head node of the linked list.
        k: Number of positions to rotate.

    Returns:
        The head node of the rotated linked list.

    """
    if k == 0 or head is None:
        return head

    count = length(head)

    if k > count:
        k = k % count

    if k == 0:
        return head

    # Find the position to rotate
    rotate_pos = count - k

    # Find the new head
    prev = None
    curr = head
    pos = 0
    while curr and pos < rotate_pos:
        prev = curr
        curr = curr.next
        pos += 1

    if prev:
        prev.next = None

    new_head = curr

    # Update connections
    while curr.next:
        curr = curr.next

    curr.next = head

    return new_head


# Test Case 1: Rotate a linked list by 2 positions
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 2
rotated_head = rotate(head, k)
# Expected output: 4 -> 5 -> 1 -> 2 -> 3
# The linked list is rotated by 2 positions, resulting in a new head with value 4.
# The new list is 4 -> 5 -> 1 -> 2 -> 3.
print_linked_list(rotated_head)  # Helper function to print the linked list

# Test Case 2: Rotate a linked list by 0 positions
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 0
rotated_head = rotate(head, k)
# Expected output: 1 -> 2 -> 3 -> 4 -> 5
# Since k is 0, the linked list remains unchanged.
# The new list is the same as the original list.
print_linked_list(rotated_head)

# Test Case 3: Rotate an empty linked list
head = None
k = 3
rotated_head = rotate(head, k)
# Expected output: None
# The linked list is empty, so there is no rotation possible.
# The output should be None.
print_linked_list(rotated_head)


# Edge Case = when k==count
