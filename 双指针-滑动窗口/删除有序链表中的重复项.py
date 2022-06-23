

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-list/submissions/
"""
def deleteDuplicates(head: ListNode) -> ListNode:
    """
    类似于【删除有序数组中的重复项】。
    因为链表没法访问前一个元素, 所以用pre指针记录快慢指针的前一个元素。
    """
    if head is None or head.next is None:
        return head
    slow_pre = head
    fast_pre = head
    slow = fast = head.next
    while fast is not None:
        if fast.val != fast_pre.val:
            slow.val = fast.val
            slow_pre = slow
            slow = slow.next
        fast_pre = fast
        fast = fast.next
    slow_pre.next = None
    return head
        