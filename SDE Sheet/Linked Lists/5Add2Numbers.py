# Own Approach - Not optimal

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    if head1 == None:
        return head2

    if head2 == None:
        return head1

    # Adding all elements into head1 linked list

    ptr = head1
    carry = 0

    # Iterate through both linked lists
    while (ptr.next and head2):
        summ = ptr.data + head2.data + carry
        if summ >= 10:
            summ = summ - 10
            carry = 1
        else:
            carry = 0

        # Update the data of the current node in head1 with the sum
        ptr.data = summ
        ptr = ptr.next
        head2 = head2.next

    # If head2 has more elements
    if head2:
        summ = ptr.data + head2.data + carry
        if summ >= 10:
            summ = summ - 10
            carry = 1
        else:
            carry = 0
        ptr.data = summ
        head2 = head2.next

        # Add the remaining elements of head2 to head1
        while (head2):
            summ = head2.data + carry
            if summ >= 10:
                summ = summ - 10
                carry = 1
            else:
                carry = 0

            # Create a new node with the sum and append it to head1
            new_node = Node(data=summ, next=None)
            ptr.next = new_node
            ptr = ptr.next
            head2 = head2.next

        # If there is still a carry remaining, create a new node with the carry value and append it to head1
        if carry == 1:
            new_node = Node(data=carry, next=None)
            ptr.next = new_node

    # If head2 has no more elements, check if there is a remaining carry
    else:
        while (ptr):
            summ = ptr.data + carry
            if summ >= 10:
                summ = summ - 10
                carry = 1
            else:
                carry = 0

            # Update the data of the current node in head1 with the sum
            ptr.data = summ
            ptr = ptr.next

    # Return the head of the modified head1 linked list
    return head1
