def delete_node(head, key):
    if not head:
        return None
    if head.data == key:
        return head.next
    current = head
    while current.next and current.next.data != key:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head

ll.head = delete_node(ll.head, 3)
ll.print_list() 