

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    根据p和q的位置来分情况:
    1. p和q在两颗子树; 或者p和q之一在根节点, 另一个节点在其中一个子树。则最近公共祖先是根节点。
    2. p和q在同一颗子树, 则递归的去处理这颗子树。

    所以问题是如何寻找p和q的位置, 通过后序遍历的方式, 寻找p和q。递归方法返回p和q是否在子树中。
    """
    def helper(root, p, q, res):
        """返回p和q之一是否在树中"""
        if root is None:
            return False
        if len(res) != 0:
            return False
        left_exist = helper(root.left, p, q, res)
        right_exist = helper(root.right, p, q, res)
        if ((root == p or root == q) and (left_exist or right_exist)) or (left_exist and right_exist):
            res.append(root)
        return root == p or root == q or left_exist or right_exist
    
    res = []
    helper(root, p, q, res)
    return res[0]