from link.types import ListNode


def reverse_m_n(head: ListNode, m: int, n: int) -> ListNode:
    """
    该函数反转以head为起点的第m个节点到第n个节点之间的部分链表，并返回新的头节点

    思路是转换为reverse_n(n-m+1)
    """
    if m == 1:
        return reverse_n(head, n)
    new_head = reverse_m_n(head.next, m-1, n-1)
    head.next = new_head
    return head


n_next_node = None # 记录第n个节点后的节点

def reverse_n(head: ListNode, n: int) -> ListNode:
    """
    该函数反转以head为起点的前n个节点，并返回新的头节点

    反转前： 1 -> 2 -> 3 -> 4 -> 5
    反转前3个
    反转后：3 -> 2 -> 1 -> 4 -> 5
    """
    if n == 1:
        global n_next_node
        n_next_node = head.next
        return head
    new_head = reverse_n(head.next, n-1)
    head.next.next = head
    head.next = n_next_node
    return new_head
