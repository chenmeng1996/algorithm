
# Definition for singly-linked list.
from heapq import heapify, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode) -> ListNode:
    """
    得研究一下归并排序
    """
    if head is None:
        return None
    l = []
    while head is not None:
        l.append(head)
        head = head.next

    l.sort(key=lambda x: x.val)
    head = l[0]
    tmp = head
    for v in l[1:]:
        tmp.next = v
        tmp = v
    tmp.next = None
    return head



if __name__ == "__main__":
    node = ListNode(4)
    tmp = node
    tmp.next = ListNode(2)
    tmp = tmp.next
    tmp.next = ListNode(1)
    tmp = tmp.next
    tmp.next = ListNode(3)
    tmp = tmp.next
    res = sortList(node)
    print(res)