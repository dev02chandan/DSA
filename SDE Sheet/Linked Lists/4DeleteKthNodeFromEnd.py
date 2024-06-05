# You performed better than 97.88% TC on my own on Coding ninjas


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeKthNode(head, k):
    if head.next == None:
        return None

    slow = head
    fast = head
    count = 1
    length = None

    # Determine the length of the linked list
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        count += 1

    # Calculate the length based on the fast pointer's position
    if fast.next == None:
        length = (count * 2) - 1
    else:
        length = count * 2

    # If k is the first node, update head and return
    if length - k == 0:
        head = head.next
        return head

    # If k is in the first half of the list
    elif count < length - k:
        while count != length - k:
            count += 1
            slow = slow.next

        # Remove the kth node
        slow.next = slow.next.next
        return head

    # If k is in the second half of the list
    else:
        slow = head
        count = 1

        while count != length - k:
            count += 1
            slow = slow.next

        # Remove the kth node
        slow.next = slow.next.next
        return head


def printLinkedList(head):
    if head is None:
        print("Empty linked list")
    else:
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Test Case 1: Remove the 3rd node (value 3)
k = 3
head = removeKthNode(head, k)
# The new linked list: 1 -> 2 -> 4 -> 5
# Print the linked list
printLinkedList(head)

# Test Case 2: Remove the 1st node (value 1)
k = 1
head = removeKthNode(head, k)
# The new linked list: 1 -> 2 -> 4
# Print the linked list
printLinkedList(head)

# Test Case 3: Remove the last node (value 5)
k = 3
head = removeKthNode(head, k)
# The new linked list: 2 -> 4
# Print the linked list
printLinkedList(head)

# Test Case 4: Remove the only remaining node (value 2)
k = 1
head = removeKthNode(head, k)
# The new linked list: 2
# Print the linked list
printLinkedList(head)
