

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.cn/problems/binary-tree-cameras/
"""
def minCameraCover(root: TreeNode) -> int:
    """
    - 若在root 处安放摄像头, 则孩子left,right 一定也会被监控到。
        此时, 只需要保证left 的两棵子树被覆盖, 同时保证right 的两棵子树也被覆盖即可。
    - 否则， 如果root 处不安放摄像头, 则除了覆盖root 的两棵子树之外, 孩子left,right 之一必须要安装摄像头,从而保证root 会被监控到。

    对于每个节点, 需要维护三种类型的状态：

    状态 a: root必须放置摄像头的情况下, 覆盖整棵树需要的摄像头数目。
    状态 b: root放置摄像头无要求, 覆盖整棵树需要的摄像头数目。
    状态 c: 不考虑root是否被监视, 覆盖两棵子树需要的摄像头数目。

    a = left_c + right_c + 1
    b = min(a, left_a + right_b, left_b + right_a)
    c = min(a, left_b + right_b)
    """
    def dfs(root: TreeNode) -> List[int]:
        if not root:
            return [float("inf"), 0, 0]
        
        left_a, left_b, left_c = dfs(root.left)
        right_a, right_b, right_c = dfs(root.right)
        a = left_c + right_c + 1
        b = min(a, left_a + right_b, left_b + right_a)
        c = min(a, left_b + right_b)
        return [a, b, c]
    
    a, b, c = dfs(root)
    return b