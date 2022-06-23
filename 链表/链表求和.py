

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
https://leetcode-cn.com/problems/sum-lists-lcci/
"""
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode()
    tmp = res
    add = 0
    while l1 is not None and l2 is not None:
        total = l1.val + l2.val + add
        tmp.next = ListNode(total % 10)
        add = total // 10
        tmp = tmp.next
        l1 = l1.next
        l2 = l2.next
    
    l3 = None
    if l1 is not None:
        l3 = l1
    if l2 is not None:
        l3 = l2
    while l3 is not None:
        total = l3.val + add
        tmp.next = ListNode(total % 10)
        add = total // 10
        tmp = tmp.next
        l3 = l3.next
    if add != 0:
        tmp.next = ListNode(add)
    return res.next
