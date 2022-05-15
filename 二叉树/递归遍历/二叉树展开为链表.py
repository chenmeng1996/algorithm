
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
"""
def flatten(root: TreeNode):
    """
    递归后序遍历。
    
    递归的将左右子树先拉平, 然后根节点与左右子树生成的链表相连。
    """
    def helper(root):
        if root is None:
            return None
        left = helper(root.left)
        right = helper(root.right)
        
        root.left = None
        if left is not None:
            # 根节点与左子树相连
            root.right = left
            # 左子树与右子树相连, 这里需要找到左子树链表的末尾
            while left.right is not None:
                left = left.right
            left.right = right
        else:
            root.right = right
        return root

    helper(root)