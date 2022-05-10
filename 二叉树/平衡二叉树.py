
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def helper(root):
        if root is None:
            return True, 0
        left_balanced, left_height = helper(root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = helper(root.right)
        if not right_balanced:
            return False, 0
        if abs(left_height - right_height) > 1:
            return False, 0
        return True, max(left_height, right_height) + 1
    
    is_balanced, _ = helper(root)
    return is_balanced