
from typing import List
from 二叉树 import TreeNode

def construct_max_tree(l: List[int]) -> TreeNode:
    """
    https://leetcode-cn.com/problems/maximum-binary-tree/

    最大二叉树定义：
    1. 二叉树的根是数组中最大元素
    2. 左子树是数组中最大值左边部分构成的最大二叉树
    3. 右子树是数组中最大值右边部分构成的最大二叉树
    """
    if len(l) == 0:
        return None
    max_index = 0
    max_value = 0
    for i, v in enumerate(l):
        if v > max_value:
            max_value = v
            max_index = i
    root = TreeNode(max_value)
    root.left = construct_max_tree(l[:max_index])
    root.right = construct_max_tree(l[max_index+1:])
    return root
