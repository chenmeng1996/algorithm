

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    从头数到第length - n个节点, 删除下一个节点即可。

    要注意如果要删除的是头节点和尾节点这两个case。
    """
    # 计算链表长度
    tmp = head
    length = 0
    while tmp is not None:
        tmp = tmp.next
        length += 1
    k = length - n
    # 删除的是头节点
    if k == 0:
        new_head = head.next
        head.next = None
        return new_head

    count = 1
    tmp = head
    while count != k:
        tmp = tmp.next
        count += 1
    # 删除的是尾节点
    if n == 1:
        tmp.next = None
        return head
    else:
        delete_node = tmp.next
        tmp.next = delete_node.next
        delete_node.next = None
        return head
    
    
