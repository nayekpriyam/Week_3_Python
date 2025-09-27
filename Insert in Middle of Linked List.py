def insert_in_middle(head, data):
    new_node = Node(data)
    if not head:
        return new_node

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    new_node.next = slow.next
    slow.next = new_node
    return head

ll = LinkedList()
for val in [1, 2, 4, 5]:
    ll.insert_at_end(val)
ll.head = insert_in_middle(ll.head, 3)
ll.print_list() 