
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/
"""
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    """
    1. 寻找反转链表的头和尾，以及前后的节点
    2. 反转部分链表
    3. 反转的链表之前是否有链表？有链表则连接before_head和right_node，并返回head。无链表则返回right_node。
    """
    # 寻找反转链表的头和尾，以及前后的节点
    tmp = head
    count = 1
    before_node = None
    after_node = None
    left_node = None
    right_node = None
    while tmp is not None:
        if count == left - 1:
            before_node = tmp
        if count == right + 1:
            after_node = tmp
        if count == left:
            left_node = tmp
        if count == right:
            right_node = tmp
        count += 1
        tmp = tmp.next
    # 反转的链表长度是否为1？
    if left_node == right_node:
        return head
    
    # 反转部分链表
    pre = after_node
    cur = left_node
    post = cur.next
    while cur != after_node:
        cur.next = pre
        pre = cur
        cur = post
        if post is not None:
            post = post.next
        
    # 反转的链表之前是否有链表？
    if before_node is not None:
        before_node.next = pre
        return head
    else:
        return right_node
    


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


if __name__ == "__main__":
    head = ListNode(1)
    tmp = head
    for i in [2,3,4,5]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    res = reverseBetween(head, 2, 4)
    print(res)