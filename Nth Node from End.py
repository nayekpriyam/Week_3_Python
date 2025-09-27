def nth_from_end(head, n):
    fast = slow = head
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.data

print(nth_from_end(ll.head, 2))  
