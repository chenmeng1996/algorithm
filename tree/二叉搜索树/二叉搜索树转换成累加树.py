from tree import *
import copy

s = 0

"""
累加树：每个节点的新值等于原树中大于或等于原节点旧值的的节点值之和。
"""
def convert(root: TreeNode) -> TreeNode:
    """二叉搜索树的中序遍历是升序，反过来就是降序"""
    new_root = copy.deepcopy(root)
    __visit(root, new_root)
    return new_root
    
def __visit(root: TreeNode, new_root: TreeNode):
    global s
    if root is None:
        return
    __visit(root.right, new_root.right)
    s += root.value
    new_root.value = s
    __visit(root.left, new_root.left)

if __name__ == "__main__":
    root = build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    new_root = convert(root)
    print_tree(new_root)

