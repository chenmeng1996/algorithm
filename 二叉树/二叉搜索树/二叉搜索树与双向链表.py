"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root: 'Node') -> 'Node':
    def helper(root):
        """
        中序遍历，对当前子树做链表操作，并返回当前子树的最小节点和最大节点
        """
        if root is None:
            return None, None
        
        cur_min, cur_max = root, root
            
        left_min, left_max = helper(root.left)
        if left_max is not None:
            left_max.right = root
            root.left = left_max
        if left_min is not None:
            cur_min = left_min

        right_min, right_max = helper(root.right)
        if right_min is not None:
            root.right = right_min
            right_min.left = root
        if right_max is not None:
            cur_max = right_max
        
        return cur_min, cur_max

    if root is None:
        return None
    first, last = helper(root)
    first.left = last
    last.right = first
    return first