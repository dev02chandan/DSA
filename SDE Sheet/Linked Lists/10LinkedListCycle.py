class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head


# utility function to create cycle
def createCycle(head, pos):
    temp = head
    ptr = head
    cnt = 0
    while temp.next != None:
        if cnt != pos:
            ptr = ptr.next
            cnt += 1
        temp = temp.next
    temp.next = ptr


def detectCycle(head):
    if head == None or head.next == None:
        return None

    slow = head
    fast = head

    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if fast.next == None or fast.next.next == None:
        return None

    fast = head
    count = 0

    while (fast != slow):
        fast = fast.next
        slow = slow.next
        count += 1

    return count


if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    # head = insertNode(head, 3)
    # head = insertNode(head, 6)
    # head = insertNode(head, 10)
    createCycle(head, 1)
    nodeRecieve = detectCycle(head)
    if nodeRecieve == None:
        print("No cycle")
    else:
        print("Tail connects at pos", nodeRecieve)
