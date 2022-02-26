from typing import Tuple
from tree import TreeNode

def traverse(root: TreeNode):
    """
    完全二叉树的一个性质：任何一个节点的左子树和右子树都是完全二叉树，且至少有一个是满二叉树。
    利用此性质，可以减少计算完全二叉树节点个数的时间复杂度。
    """
    num = _traverse(root)
    print(num)

def _traverse(root: TreeNode) -> int:
    if root is None:
        return 0
    left_total = 0
    height, ok = _is_full_tree(root.left)
    if ok:
        # 利用满二叉树的高度快速计算节点个数
        left_total = 2 ** height - 1
    else:
        left_total = _traverse(root.left)
    right_total = 0
    height, ok = _is_full_tree(root.right)
    if ok:
        right_total = 2 ** height - 1
    else:
        right_total = _traverse(root.right)
    return 1 + left_total + right_total


def _is_full_tree(root: TreeNode) -> Tuple[int, bool]:
    """是否是满二叉树"""
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
