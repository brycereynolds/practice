def has_cycle(head):

    fast = head
    slow = head

    while fast.next != None:

        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

        if slow == fast:
            return True

    return False