"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
import collections
import copy
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
"""
def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    """
    层序遍历，在记录一层内容时反序即可。
    """
    if root is None:
        return []
    que = collections.deque()
    que.append(root)
    res = []
    turn = False
    while que:
        level = collections.deque()
        for _ in range(len(que)):
            x = que.popleft()
            if x.left is not None:
                que.append(x.left)
            if x.right is not None:
                que.append(x.right)
            if not turn:
                level.append(x.val)
            else:
                level.appendleft(x.val)
        res.append(list(copy.copy(level)))
        level.clear()
        turn = not turn
    return res