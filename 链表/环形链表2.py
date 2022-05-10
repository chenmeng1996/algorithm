# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/submissions/
"""
def detectCycle(head: ListNode) -> ListNode:
    """
    1. 快慢指针，找到两指针相遇的位置。
    2. 然后，头指针从头开始移动，慢指针从两指针相遇的地方开始移动，最终会在环处相遇。
    """
    if head is None:
        return None
    i, j = head, head
    flag = False
    while i != j or not flag:
        flag = True
        if i is None or j is None:
            return None
        if j.next is None:
            return None
        i = i.next
        j = j.next.next
    while head != i:
        head = head.next
        i = i.next
    return i