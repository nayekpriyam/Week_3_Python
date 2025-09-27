def remove_loop(head):
    slow = fast = head
    loop_exists = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break

    if not loop_exists:
        return head

    slow = head
    prev = None
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next
    prev.next = None
    return head 