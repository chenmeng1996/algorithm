

from tree import TreeNode


def invert_tree(root: TreeNode):
    """
    将root为根的二叉树反转，返回新的root。

    思路是递归的将左右子树反转，并反转当前节点的左右子节点。
    """
    if root is None:
        return
    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left