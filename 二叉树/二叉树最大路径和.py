
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
"""
def maxPathSum(root: TreeNode) -> int:
    """
    遍历节点，并计算以每个节点为根节点的单向最大路径和（只能可选的取一个子树的最大路径）和最大路径和（可以可选的取两个子树的最大路径和）。
    """    
    def helper(root, res):
        """
        函数返回
        """
        if root is None:
            return 0
        left_single_max = helper(root.left, res)
        right_single_max = helper(root.right, res)
        res[0] = max(res[0], left_single_max+right_single_max+root.val, left_single_max+root.val, right_single_max+root.val, root.val)
        return max(left_single_max+root.val, right_single_max+root.val, root.val)
    res = [float("-inf")]
    helper(root, res)
    return res[0]