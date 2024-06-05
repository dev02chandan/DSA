# Better Solutin - on my own

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(firstHead, secondHead):
    if firstHead == None or secondHead == None:
        return None

    dummy1 = firstHead
    dummy2 = secondHead

    while (dummy1 != dummy2):
        if dummy1 == None:
            dummy1 = secondHead
        else:
            dummy1 = dummy1.next

        if dummy2 == None:
            dummy2 = firstHead
        else:
            dummy2 = dummy2.next

    return dummy1


# Test Case 1: Linked lists have an intersection
# Expected Output: Intersection Node with data = 4
head1 = Node(1)
node2 = Node(2)
node3 = Node(3)
intersectNode = Node(4)
node5 = Node(5)
node6 = Node(6)

head2 = Node(7)
node8 = Node(8)

head1.next = node2
node2.next = node3
node3.next = intersectNode
intersectNode.next = node5
node5.next = node6

head2.next = node8
node8.next = intersectNode

result = findIntersection(head1, head2)
if result:
    print("Test Case 1: Passed. Intersection Node with data =", result.data)
else:
    print("Test Case 1: Failed. No Intersection Node found.")

# Test Case 2: Linked lists have no intersection
# Expected Output: None
head1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head2 = Node(4)
node5 = Node(5)
node6 = Node(6)

head1.next = node2
node2.next = node3

head2.next = node5
node5.next = node6

result = findIntersection(head1, head2)
if result is None:
    print("Test Case 2: Passed. No Intersection Node found.")
else:
    print("Test Case 2: Failed. Intersection Node with data =", result.data)

# Test Case 3: Linked lists are the same
# Expected Output: The head of the linked lists
head1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head2 = head1

result = findIntersection(head1, head2)
if result == head1:
    print("Test Case 3: Passed. Same Linked List, Intersection at head.")
else:
    print("Test Case 3: Failed.")
