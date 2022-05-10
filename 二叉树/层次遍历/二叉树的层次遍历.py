from 二叉树 import TreeNode
from queue import Queue

def recursion(root: TreeNode):
    q = Queue()
    res = []
    _recursion(root, q, res)
    
def _recursion(root: TreeNode, q: Queue, res: list):
    if root is None:
        return
    res.append(root.value)
    q.put(root.left)
    q.put(root.right)