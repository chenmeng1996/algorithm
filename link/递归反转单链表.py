from link.types import ListNode


def reverse(head: ListNode) -> ListNode:
    """
    reverse函数将head为起点的链表反转，最后一个node指向null，并返回新的head
    """
    if head.next == None:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last