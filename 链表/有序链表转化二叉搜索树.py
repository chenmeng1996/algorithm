# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
"""
def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    """
    分治。

    寻找链表中点，将链表分为两半，构造二叉搜索树的左右子树。左右链表继续递归构造二叉搜索树。

    可以在分治的基础上，使用中序遍历进行优化。
    """
    def find_middle(left, right):
        
        slow = fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def build_tree(head, tail):
        # 检查左右区间，左闭右开
        if head == tail:
            return None
        mid = find_middle(head, tail)
        root = TreeNode(mid.val)
        root.left = build_tree(head, mid)
        root.right = build_tree(mid.next, tail)
        return root
    
    return build_tree(head, None)


if __name__ == "__main__":
    head = ListNode(-10)
    tmp = head
    for i in [-3,0,5,9]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    res = sortedListToBST(head)
    print(res)