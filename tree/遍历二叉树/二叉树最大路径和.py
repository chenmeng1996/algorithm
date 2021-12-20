import sys
from tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """124. 二叉树最大路径和"""
        self.ans = -sys.maxsize
        self._one_side_max(root)
        return self.ans

    def _one_side_max(self, root: TreeNode):
        """二叉树最大路径和"""
        if not root:
            return 0
        v = root.value
        left_max = max(0, self._one_side_max(root.left))
        right_max = max(0, self._one_side_max(root.right))
        self.ans = max(self.ans, left_max + right_max + v)
        return max(left_max, right_max) + root.value


if __name__ == "__main__":
    root = build_tree([-10, 9, 20, None, None, 15, 7])
    so = Solution()
    print(so.maxPathSum(root))