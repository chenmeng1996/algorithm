

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
"""
def maxDepth(root: TreeNode) -> int:
    """
    子树的深度 = max(左子树深度,右子树深度) + 1
    递归。
    """
    def helper(root):
        """返回树的深度"""
        if root is None:
            return 0
        return 1 + max(helper(root.left), helper(root.right))
    return helper(root)