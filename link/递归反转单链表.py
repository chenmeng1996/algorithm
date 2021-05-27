from link.types import ListNode


def reverse1(head: ListNode) -> ListNode:
    """
    递归的将head为起点的链表反转，最后一个node指向null，并返回新的head
    """
    if head.next == None:
        return head
    last = reverse1(head.next)
    head.next.next = head
    head.next = None
    return last

def reverse2(head: ListNode):
    """
    非递归的将head为头的链表反转，返回新的head
    """
    pre = None
    while head is not None:
        '''
        每一轮将head指向pre，并向后移动一位
        '''
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre