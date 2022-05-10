# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    def check(a, b):
            if b is None:
                return True
            if a is None:
                return False
            if a.val != b.val:
                return False
            return check(a.left, b.left) and check(a.right, b.right)
    
    def traverse(a, b):
        if a is None:
            return False
        if check(a, b):
            return True
        if traverse(a.left, b):
            return True
        if traverse(a.right, b):
            return True 
        return False
    if B is None:
        return False
    return traverse(A, B)