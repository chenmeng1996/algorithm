
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
https://leetcode.cn/problems/reverse-nodes-in-k-group/
"""
def reverse_k(head: ListNode, k: int) -> ListNode:
    """
    递归。
    将链表的前k个进行反转，第一次pre指针指向 递归反转后的链表的头指针。
    """
    def reverse(head):
        if head is None:
            return None
        count = 0
        tmp = head
        while tmp is not None and count < k:
            count += 1
            tmp = tmp.next
        if count != k:
            return head
        # 递归反转后面的链表，并将pre指向它
        pre = reverse(tmp)
        # 接下来反转当前的一段链表
        cur = head
        post = head.next
        count = 0
        while cur is not None and count < k:
            cur.next = pre
            pre = cur
            cur = post
            if post is not None:
                post = post.next
            count += 1
        return pre
        
    return reverse(head)


if __name__ == "__main__":
    a = ListNode(1)
    tmp = a
    for i in [2,3,4,5]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    res = reverse_k(a, 3)
    while res is not None:
        print(res.val)
        res = res.next