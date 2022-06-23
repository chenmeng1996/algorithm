from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    左子树的根节点比root节点小，右子树的根节点比root节点大。
    递归下去，所有子树都满足该定义即可。
    """
    def helper(root, lower=float("-inf"), upper=float("inf")):
        if root is None:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        if not helper(root.left, lower, root.val):
            return False
        if not helper(root.right, root.val, upper):
            return False
        return True
    return helper(root)