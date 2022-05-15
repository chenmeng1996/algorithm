from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
"""   
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    递归中序遍历
    """
    def traverse(root, res, count):
        if root is None or len(res) != 0:
            return
        traverse(root.left, res, count)
        count[0] += 1
        if count[0] == k:
            res.append(root.val)
        traverse(root.right, res, count)
    
    res = []
    count = [0]
    traverse(root, res, count)
    if res:
        return res[0]
    else:
        return None
