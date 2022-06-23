from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/count-complete-tree-nodes/
"""
def countNodes(root: TreeNode):
    """
    完全二叉树的一个性质：任何一个节点的左子树和右子树都是完全二叉树，且至少有一个是满二叉树。
    利用此性质，可以减少计算完全二叉树节点个数的时间复杂度。

    
    因为树的高度为logn，所以判断是否是满二叉树的时间复杂度是O(logn)，
    因为每次至少有一个子树是满二叉树，所以只需要对另一个子树递归计算，所以递归次数是O(logn)
    所以时间复杂度：O((logn)^2)
    """
    def is_full_tree(root: TreeNode) -> Tuple[int, bool]:
        """
        完全二叉树是否是满二叉树。
        通过一直向左遍历，一直向右遍历，判断长度是否相等。
        """
        left_height = 0
        right_height = 0
        tmp = root
        while tmp is not None:
            left_height += 1
            tmp = tmp.left
        tmp = root
        while tmp is not None:
            right_height += 1
            tmp = tmp.right
        return left_height, left_height == right_height
        
    def helper(root: TreeNode) -> int:
        if root is None:
            return 0
        left_total = 0
        # 左子树是否是满二叉树
        height, ok = is_full_tree(root.left)
        if ok:
            # 利用满二叉树的高度快速计算节点个数
            left_total = 2 ** height - 1
        else:
            # 左子树不是满二叉树，只是完全二叉树，则递归进行计算。
            left_total = helper(root.left)
        # 右子树同理
        right_total = 0
        height, ok = is_full_tree(root.right)
        if ok:
            right_total = 2 ** height - 1
        else:
            right_total = helper(root.right)
        return 1 + left_total + right_total

    return helper(root)
