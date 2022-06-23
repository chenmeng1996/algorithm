

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode.cn/problems/insert-into-a-binary-search-tree/
"""
def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    """
    查找, 并插入即可。
    """
    if root is None:
        return TreeNode(val)
    tmp = father = root
    flag = 0
    while tmp:
        father = tmp
        if val < tmp.val :
            tmp = tmp.left
            flag = -1
        else:
            tmp = tmp.right
            flag = 1
    if flag == -1:
        father.left = TreeNode(val)
    else:
        father.right = TreeNode(val)
    return root