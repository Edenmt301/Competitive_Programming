def has_cycle(head):
    slow=head
    fast=head.next
    while slow!=fast:
        if not fast or not fast.next:
            return 0
        slow=slow.next
        fast=fast.next.next
    return 1 
