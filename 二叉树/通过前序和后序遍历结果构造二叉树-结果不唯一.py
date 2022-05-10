from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        pre_set = set([preorder[1]])
        post_set = set([postorder[0]])
        i = 1
        while pre_set != post_set:
            pre_set.add(preorder[i+1])
            post_set.add(postorder[i])
            i += 1
        root.left = self.constructFromPrePost(preorder[1:i+1], postorder[:i])
        root.right = self.constructFromPrePost(preorder[i+1:], postorder[i:])
        return root