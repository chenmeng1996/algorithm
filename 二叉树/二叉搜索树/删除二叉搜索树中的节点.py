# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    1. 如果删除的key在左子树，则递归在左子树删除key，并更新当前节点的左子树。
    2. 如果删除的key在右子树，则递归在右子树删除key，并更新当前节点的右子树。
    3. 如果删除的key是当前root节点，则
        1. 如果删除的节点是叶子结点，则直接删除。并返回None。
        2. 如果删除的节点有右孩子，则寻找后继节点，然后用后继节点的值覆盖当前节点，并递归的在右子树删除后继节点，更新当前节点的右孩子，并返回当前节点。
        3. 如果删除的节点没有右孩子，则寻找前继节点，然后用前继节点的值覆盖当前节点，并递归的在左子树删除前继节点，更新当前节点的左孩子，并返回当前节点。
    """
    def predecessor(root):
        """
        寻找前继节点：进入当前节点的左节点，并一直往右寻找。
        （如果没有左节点，则前继节点是自身或者父节点）
        """
        if root.left is None:
            return None
        root = root.left
        while root.right is not None:
            root = root.right
        return root
    
    def accessor(root):
        """
        寻找后继节点：进入当前节点的右节点，并一直往左寻找。
        （如果没有右节点，则后继节点为自身或者父节点，这取决于当前节点是父节点的左孩子还是右孩子。
        在本题中，这里如果没有右节点，就去找前继节点了）
        """
        if root.right is None:
            return None
        root = root.right
        while root.left is not None:
            root = root.left
        return root
    
    def helper(root, key):
        if root is None:
            # 删除的key找不到
            return root
        if key > root.val:
            # key在右子树
            root.right = helper(root.right, key)
        elif key < root.val:
            # key在左子树
            root.left = helper(root.left, key)
        else:
            # key在root节点
            # key是叶子节点，叶子节点删除
            if root.left is None and root.right is None:
                root =  None
            # key有右孩子, 则寻找中序遍历的后继节点, 交换节点值, 并在右子树递归删除后继节点
            elif root.right is not None:
                post = accessor(root)
                root.val = post.val
                root.right = helper(root.right, post.val)
            # 如果没有右孩子, 则寻找中序遍历的前继节点, 交换节点值，并在左子树递归删除前继节点
            else:
                pre = predecessor(root)
                root.val = pre.val
                root.left = helper(root.left, pre.val)
        return root

    return helper(root, key)