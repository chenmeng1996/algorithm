
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
https://leetcode-cn.com/problems/sort-list/

要求时间复杂度: O(nlogn), 空间复杂度为常数
"""
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    归并排序。
    1. 快慢指针寻找中间指针，并断开连接（或者指定开始和结束的节点）。
    2. 递归的将两个链表归并排序。
    3. 将排序好的两个链表合并。
    """
    def merge(head1, head2):
        new_head = ListNode()
        tmp = new_head
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                tmp.next = head1
                tmp = tmp.next
                head1 = head1.next
            else:
                tmp.next = head2
                tmp = tmp.next
                head2 = head2.next
        if head1 is not None:
            tmp.next = head1
        if head2 is not None:
            tmp.next = head2
        return new_head.next

    def find_middle(head):
        if head is None:
            return None
        slow = head
        fast = head
        pre_mid = slow
        while fast is not None and fast.next is not None:
            pre_mid = slow
            slow = slow.next
            fast = fast.next.next
        return pre_mid

    def helper(head):
        if head is None or head.next is None:
            return head
        middle = find_middle(head)
        if middle is not None:
            nex = middle.next
            middle.next = None
        else:
            nex = None
        return merge(helper(head), helper(nex))
    
    return helper(head)
        

def sortList1(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    从底向上归并排序 TODO
    """
    def merge(head1: ListNode, head2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummyHead.next
    
    if not head:
        return head
    
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    
    dummyHead = ListNode(0, head)
    subLength = 1
    while subLength < length:
        prev, curr = dummyHead, dummyHead.next
        while curr:
            head1 = curr
            for i in range(1, subLength):
                if curr.next:
                    curr = curr.next
                else:
                    break
            head2 = curr.next
            curr.next = None
            curr = head2
            for i in range(1, subLength):
                if curr and curr.next:
                    curr = curr.next
                else:
                    break
            
            succ = None
            if curr:
                succ = curr.next
                curr.next = None
            
            merged = merge(head1, head2)
            prev.next = merged
            while prev.next:
                prev = prev.next
            curr = succ
        subLength <<= 1
    
    return dummyHead.next


if __name__ == "__main__":
    head = ListNode(3)
    tmp = head
    for i in [4,1,5,2]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    res = sortList(head)
    print(res)