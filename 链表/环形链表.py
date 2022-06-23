

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
https://leetcode-cn.com/problems/linked-list-cycle/
"""
def hasCycle(head: Optional[ListNode]) -> bool:
    """
    快慢指针，快指针如果等于慢指针，则有环。
    """
    i = j = head
    flag = False
    while i != j or not flag:
        flag = True
        if i is None or j is None:
            return False
        if j.next is None:
            return False
        i = i.next
        j = j.next.next
    return True