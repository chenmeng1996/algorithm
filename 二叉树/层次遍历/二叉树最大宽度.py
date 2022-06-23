from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
https://leetcode.cn/problems/maximum-width-of-binary-tree/
"""
def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    层序遍历。
    队列在记录节点的同时也记录索引。
    root节点的索引为i, 左右孩子的索引为2*i+1和2*i+2
    """
    if root is None:
        return 0
    que = deque()
    que.append((root, 0))
    res = 0
    while que:
        if len(que) == 1:
            res = max(res, 1)
        else:
            res = max(res, que[-1][1] - que[0][1] + 1)
        for _ in range(len(que)):
            x, index = que.popleft()
            if x.left is not None:
                que.append((x.left, 2*index+1))
            if x.right is not None:
                que.append((x.right, 2*index+2))
    return res