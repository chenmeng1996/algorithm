



from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/
"""
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    分治合并，两两合并单链表
    """
    def merge(head1, head2):
        new_head = ListNode()
        tmp = new_head
        while head1 is not None and head2 is not None:
            if head1.val > head2.val:
                tmp.next = head2
                head2 = head2.next
            else:
                tmp.next = head1
                head1 = head1.next
            tmp = tmp.next
        if head1 is not None:
            tmp.next = head1
        if head2 is not None:
            tmp.next = head2
        return new_head.next

    def helper(lists, start, end):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = helper(lists, start, mid)
        right = helper(lists, mid+1, end)
        return merge(left, right)
    
    return helper(lists, 0, len(lists)-1)
        