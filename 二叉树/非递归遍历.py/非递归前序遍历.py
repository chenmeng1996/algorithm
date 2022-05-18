

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/binary-tree-preorder-traversal/
"""
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    栈。
    栈顶节点出栈并访问, 然后将该节点的右孩子、左孩子依次入栈。
    """
    stack = []
    if root is None:
        return []
    stack.append(root)
    res = []
    while stack:
        t = stack.pop()
        res.append(t.val)
        if t.right is not None:
            stack.append(t.right)
        if t.left is not None:
            stack.append(t.left)
    return res
