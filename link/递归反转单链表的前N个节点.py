from link.types import ListNode


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
