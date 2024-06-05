def deleteNode(node):
    nextNode = node.next

    node.data = nextNode.data

    node.next = nextNode.next

    del nextNode
