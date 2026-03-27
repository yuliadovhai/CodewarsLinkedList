from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    prev = None
    current = head

    while current is not None and current.next is not None:
        first = current
        second = current.next
        next_pair = second.next

        second.next = first

        if prev is not None:
            prev.next = second

        if next_pair is not None and next_pair.next is not None:
            first.next = next_pair.next
        else:
            first.next = next_pair

        prev = first
        current = next_pair

    return new_head
