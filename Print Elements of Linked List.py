def print_linked_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next

print_linked_list(ll.head) 