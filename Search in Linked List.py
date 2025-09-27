def search(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False

print(search(ll.head, 4)) 
print(search(ll.head, 10)) 