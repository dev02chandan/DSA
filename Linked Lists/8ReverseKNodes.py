# Leetcode Hard - 1st time

# Following is the class structure of the Node class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getListAfterReverseOperation(head, n, b):
    if not head:
        return None

    # Create a dummy node to handle the case of reversing the first segment
    node = Node(0)
    node.next = head
    curr = head  # to calculate the length of the list
    prev = node
    nexxt = None
    count = 0

    # Using Curr to find the length
    while curr and curr.next:
        curr = curr.next.next
        count += 1

    if curr is None:
        count *= 2
    else:
        count = count * 2 + 1

    # count holds the length of the linked list

    curr = None  # reset curr

    # Reverse segments based on the list 'b'
    for i in b:
        curr = prev.next
        nexxt = curr.next
        if i > count:
            k = count
        elif i == 0:
            continue  # Skip reversing if segment size is 0
        else:
            k = i

        # Reverse the segment by adjusting the next pointers
        for j in range(k - 1):
            curr.next = nexxt.next
            nexxt.next = prev.next
            prev.next = nexxt
            nexxt = curr.next

        count -= k
        prev = curr

        if count <= 0:
            break  # Stop reversing if the remaining length is less than or equal to 0

    return node.next


'''
The code aims to reverse segments of a linked list based on the values in the list b. Here's a summary of the code:

The getListAfterReverseOperation function takes a linked list head node, the total length of the list (n), and a list of segment sizes (b).

It initializes a dummy node (node) and connects it to the head node. This dummy node helps handle the case of reversing the first segment.

It calculates the length of the linked list by traversing it using curr pointer, counting each node and incrementing by 1 for every two nodes.

If the length is odd, it updates the count variable accordingly.

It then resets the curr pointer to None before reversing the segments.

The code iterates through the list b and performs segment reversals based on the segment sizes specified.

Within each segment, it adjusts the next pointers to reverse the nodes.

It updates the count and prev pointers accordingly.

If the remaining length (count) is less than or equal to 0, the process stops.

Finally, it returns the modified linked list with the reversed segments.

Please note that this code assumes the linked list is 1-indexed.
'''


def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Test Case 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

result = getListAfterReverseOperation(head, 6, [2, 3])
print("Output:")
printLinkedList(result)
# Expected Output: 2 -> 1 -> 5 -> 4 -> 3 -> 6 -> None

# Test Case 2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = getListAfterReverseOperation(head, 5, [5])
print("Output:")
printLinkedList(result)
# Expected Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Test Case 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

result = getListAfterReverseOperation(head, 4, [2, 0, 1])
print("Output:")
printLinkedList(result)
# Expected Output: 2 -> 1 -> 3 -> 4 -> None
