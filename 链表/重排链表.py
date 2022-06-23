

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
https://leetcode-cn.com/problems/reorder-list/
"""
def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.

    数组记录链表节点（线性表），然后重排链表即可。

    空间O(1)的方法是将链表分成两半，后一半逆序，然后合并链表。
    """
    arr = []
    tmp = head
    while tmp is not None:
        arr.append(tmp)
        tmp = tmp.next
    i = 1
    j = len(arr)-1
    reverse = True
    tmp = head
    while i <= j:
        if reverse:
            tmp.next = arr[j]
            j -= 1
            reverse = False
        else:
            tmp.next = arr[i]
            i += 1
            reverse = True
        tmp = tmp.next
    # 尾节点指向None，防止循环链表
    tmp.next = None
    return head


if __name__ == "__main__":
    head = ListNode(1)
    tmp = head
    for i in [2,3,4]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    reorderList(head)
    print(head)
    