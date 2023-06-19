class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(firstHead, secondHead):
    myset = set()
    if firstHead == secondHead:
        return firstHead
    myset.add(firstHead)
    myset.add(secondHead)

    while (firstHead.next != None and secondHead.next != None):
        if firstHead.next in set:
            return firstHead.next

        firstHead = firstHead.next
        myset.add(firstHead)

        if secondHead.next in set:
            return secondHead.next

        secondHead = secondHead.next
        myset.add(secondHead)

    while (firstHead.next != None):
        if firstHead.next in set:
            return firstHead.next

        firstHead = firstHead.next

    while (secondHead.next != None):
        if secondHead.next in set:
            return secondHead.next

        secondHead = secondHead.next

    return None


Node1 = Node(1)
Node1.next = Node(2)

myset = set()

myset.add(Node1)
print(myset)
