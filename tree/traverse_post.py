import sys

from tree import *

import unittest


class TestTree(unittest.TestCase):
    def test_max_path_sum(self):
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        so = Solution()
        print(so.maxPathSum(root))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        v = root.val
        left_max = max(0, self._one_side_max(root.left))
        right_max = max(0, self._one_side_max(root.right))
        self.ans = max(self.ans, left_max + right_max + v)
        return max(left_max, right_max) + root.val


def build_tree(values):
    root = TreeNode()
    nodes = []
    for i in range(len(values)):
        if i == 0:
            root.val = values[i]
            nodes.append(root)
            continue
        # 构造新节点
        new_node = TreeNode(val=values[i]) if values[i] else None
        nodes.append(new_node)
        # 新节点的父节点索引
        parent_index = (i - 1) // 2
        if i % 2 != 0:
            nodes[parent_index].left = new_node
        else:
            nodes[parent_index].right = new_node
    return root
