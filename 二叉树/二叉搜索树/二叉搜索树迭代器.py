# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        tmp = root
        while tmp is not None:
            self.stack.append(tmp)
            tmp = tmp.left

    def next(self) -> int:
        if len(self.stack) == 0:
            return -1
        res = self.stack.pop()
        if res.right is not None:
            tmp = res.right
            while tmp is not None:
                self.stack.append(tmp)
                tmp = tmp.left
        return res.val
        

    def hasNext(self) -> bool:
        return len(self.stack) != 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()