from typing import Deque, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/binary-tree-right-side-view/
"""
def rightSideView(root: TreeNode) -> List[int]:
    """
    层次遍历, 输出每层元素的最后一个
    层次遍历的重点：每次把队列清空，就是一层
    """
    if root is None:
        return []
    que = Deque()
    que.append(root)
    res = []
    while que:
        length = len(que)
        for i in range(length):
            rt = que.popleft()
            # 每层的最后一个元素
            if i == length - 1:
                res.append(rt.val)
            if rt.left is not None:
                que.append(rt.left)
            if rt.right is not None:
                que.append(rt.right)
    return res
