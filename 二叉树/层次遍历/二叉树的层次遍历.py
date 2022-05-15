from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""
def levelOrder(root: TreeNode):
    if root is None:
        return []
    que = deque()
    res = []
    que.append(root)
    while que:
        cur = []
        for _ in range(len(que)):
            x = que.popleft()
            cur.append(x.val)
            if x.left is not None:
                que.append(x.left)
            if x.right is not None:
                que.append(x.right)
        res.append(cur)
    return res