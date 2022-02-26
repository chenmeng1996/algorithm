
from tree import TreeNode


def is_binary_search_tree(root: TreeNode) -> bool:
    return _is_binary_search_tree(root, None, None)

def _is_binary_search_tree(root: TreeNode, max: TreeNode, min: TreeNode) -> bool:
    if root is None:
        return True
    if root.left is not None and root.left.value > root.value:
        return False
    if root.right is not None and root.right.value < root.value:
        return False
    if max is not None and root.left.value > max.value:
        return False
    if min is not None and root.right.value < min.value:
        return False
    return _is_binary_search_tree(root.left, root, None) and _is_binary_search_tree(root.right, None, root)