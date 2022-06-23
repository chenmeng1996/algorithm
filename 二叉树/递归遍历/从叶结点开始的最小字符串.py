

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://leetcode.cn/problems/smallest-string-starting-from-leaf/
"""
def smallestFromLeaf(root):
    """
    树的dfs遍历
    """
    ans = "~"
    def dfs(node, A):
        if node:
            A.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                ans = min(ans, "".join(reversed(A)))

            dfs(node.left, A)
            dfs(node.right, A)
            A.pop()

    dfs(root, [])
    return ans

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    """
    非递归的后序遍历。
    使用栈记录当前节点, 使用set记录已经访问的节点。当访问到叶子节点时, 栈元素即是根节点到叶子节点的路径。
    """
    if root is None:
        return ""
    stack = [root]
    visited = set()
    res = None
    while stack:
        x = stack[-1]
        if x.left is not None and x.left not in visited:
            stack.append(x.left)
        elif x.right is not None and x.right not in visited:
            stack.append(x.right)
        else:
            if x.left is None and x.right is None:
                vals = [chr(node.val+97) for node in stack]
                vals.reverse()
                if res is None:
                    res = "".join(vals)
                else:
                    res = min(res, "".join(vals))
            stack.pop()
            visited.add(x)
    return res
