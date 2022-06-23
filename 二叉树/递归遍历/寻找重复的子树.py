import collections
from typing import Any, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.cn/problems/find-duplicate-subtrees/

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。
"""
def find_duplicate_subtrees(root: TreeNode) -> List[TreeNode]:
    """
    先序遍历，返回子树的序列化列表
    """
    record = {}
    res = []
    def serialize(root: TreeNode) -> List[Any]:
        if root is None:
            return "#"
        join = "{},{},{}".format(root.value, serialize(root.left), serialize(root.right))
        if join in record:
            record[join] += 1
        else:
            record[join] = 1
        if record[join] == 2:
            res.append(root)
        return join
    serialize(root)
    return res

def find_duplicate_subtrees_with_counter(root: TreeNode) -> List[TreeNode]:
    """
    先序遍历，返回子树的序列化列表
    """
    record = collections.Counter()
    res = []
    def serialize(root: TreeNode) -> List[Any]:
        if root is None:
            return "#"
        join = "{},{},{}".format(root.value, serialize(root.left), serialize(root.right))
        record[join] += 1
        if record[join] == 2:
            res.append(root)
        return join
    serialize(root)
    return res

def find_duplicate_subtrees_2(root: TreeNode) -> List[TreeNode]:
    """
    """
    pass