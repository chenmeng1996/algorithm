
from typing import List
from tree.types import TreeNode

def build_tree(pre: List[int], mid: List[int]) -> TreeNode:
    if len(pre) == 0:
        return None
    root = TreeNode(pre[0])
    i = mid.index(pre[0])
    root.left = build_tree(pre[0:i+1], mid[:i])
    root.right = build_tree(pre[i+2:], mid[i+1:])
    return root