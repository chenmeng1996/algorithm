
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode-cn.com/problems/maximum-binary-tree/
"""
def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    """
    递归前序遍历。
    """
    def helper(nums, start, end):
        if start > end:
            return None
        max_index = 0
        max_value = float("-inf")
        for i in range(start, end+1):
            v = nums[i]
            if v > max_value:
                max_value = v
                max_index = i
        root = TreeNode(max_value)
        root.left = helper(nums, start, max_index-1)
        root.right = helper(nums, max_index+1, end)
        return root
    
    return helper(nums, 0, len(nums)-1)
