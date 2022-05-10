
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    递归。
    递归的构造左子树和右子树。
    TODO 使用左右指针代替数组复制。
    """
    def helper(preorder: List[int], inorder: List[int]):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break

        root.left = helper(preorder[1:1+index], inorder[:index])
        root.right = helper(preorder[1+index:], inorder[index+1:])
        return root
    
    return helper(preorder, inorder)