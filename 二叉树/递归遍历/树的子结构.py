# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
"""
def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    """
    递归前序遍历。
    遍历A的所有子树, 和B进行比较。
    """
    def check(root1, root2):
        """递归前序遍历, 检查root2是否是root1的子结构"""
        if root2 is None:
            return True
        if root1 is None:
            if root1 == root2:
                return True
            else:
                return False
        if root1.val == root2.val:
            return check(root1.left, root2.left) and check(root1.right, root2.right)
        else:
            return False

    def helper(root1, root2):
        """遍历root1的每个子树, 与root2进行比较"""
        if root1 is None:
            return False
        if check(root1, root2):
            return True
        if helper(root1.left, root2):
            return True
        if helper(root1.right, root2):
            return True
        return False
    
    if B is None:
        return False
    return helper(A, B)