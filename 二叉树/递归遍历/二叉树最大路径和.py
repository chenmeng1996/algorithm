
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
    递归后序遍历。
    递归函数返回子树在选取根节点下的单向最大路径和。
    在递归过程中, 记录每个子树的双向最大路径和（包含根节点）, 计算子树的双向最大路径和的最大值, 就是答案。因为最大路径和也是属于某个子树的。

    包含根节点的最大路径和为 max(root, root+左子树选取根节点的最大路径和, root+右子树选取根节点的最大路径和 , root+左子树选取根节点的最大路径和+右子树选取根节点的最大路径和)
    """    
    def helper(root, res):
        """返回子树在选取根节点下的单向最大路径和"""
        if root is None:
            return 0
        left_max = helper(root.left, res)
        right_max = helper(root.right, res)
        res[0] = max(res[0], root.val, left_max+root.val, right_max+root.val, left_max+right_max+root.val)
        return max(root.val, left_max+root.val, right_max+root.val)

    res = [float("-inf")]
    helper(root, res)
    return res[0]