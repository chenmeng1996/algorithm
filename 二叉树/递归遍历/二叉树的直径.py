
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode-cn.com/problems/diameter-of-binary-tree/
"""
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    最大直径有两种情况：
    1. 经过根节点，res = 左子树的深度 + 右子树的深度 + 1
    2. 不经过根节点，res = max(左子树的最大直径, 右子树的最大直径)
    两种情况都计算，取较大者。
    """
    def helper(root, res):
        """返回树的深度"""
        if root is None:
            return 0
        left_len = helper(root.left, res)
        right_len = helper(root.right, res)
        res[0] = max(res[0], left_len + right_len + 1)
        return max(left_len+1, right_len+1)
    
    res = [0]
    helper(root, res)
    return res[0] - 1