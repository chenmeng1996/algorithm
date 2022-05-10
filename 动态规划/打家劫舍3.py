
from typing import List

a = {}
a[None] = 0
print(a)
print(a[None])

"""
房屋组成了一个二叉树。
不可以偷相连的房子。
"""
def rob(root: TreeNode) -> int:
    """
    f[i]表示以i节点为根节点, 选择i节点偷的最大金额.
    g[i]表示以i节点为根节点, 不选择i节点偷的最大金额.
    l为i节点的左节点 r为i节点的右节点

    f[i] = g[l] + g[r]
    g[i] = max(f[l], g[l]) + max(f[r], g[r])
    """
    f = {}
    g = {}
    f[None] = 0
    g[None] = 0

    def dfs(root):
        if root is None:
            return
        dfs(root.left)
        dfs(root.right)
        f[root] = g[root.left] + g[root.right]
        g[root] = max(f[root.left], g[root.left]) + max(f[root.right], g[root.right])
    
    dfs(root)
    return max(f[root], g[root])
    