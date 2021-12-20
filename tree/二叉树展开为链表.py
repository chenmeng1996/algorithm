from tree import TreeNode

def flatten(root: TreeNode):
    """
    该函数将root为节点的树拉平成链表
    """
    if root is None:
        return
    flatten(root.left)
    flatten(root.right)
    
    # 左子树移动到右子树
    left = root.left
    right = root.right
    root.right = left
    root.left = None
    
    # 旧右子树连接到新右子树
    while left.right is not None:
        left = left.next
    left.next = right