from link.types import ListNode


def reverse_k(head: ListNode, k: int) -> ListNode:
    """
    该函数将head开头的链表，每k个节点为一组进行反转，并返回新head
    """
    tail = head
    next = head.next
    for _ in range(k):
        tail = tail.next
    new_head = reverse(head, tail)
    head.next = reverse_k(next)

def reverse(head: ListNode, tail: ListNode) -> ListNode:
    """
    非递归的将[head,tail)链表反转，返回新的head，
    注意tail是开区间。
    """
    pre = None
    while head != tail:
        '''
        每一轮将head指向pre，并向后移动一位
        '''
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre