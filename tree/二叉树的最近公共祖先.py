from tree import TreeNode

def solution_1(root: TreeNode, p, q) -> TreeNode: 
    ans = None
    _solution_1(root, p, q, ans, False)

def _solution_1(root: TreeNode, p, q, ans) -> bool:
    if root is None:
        return False
    if ans is not None: # 已经得到结果，跳出递归
        return False
    left_has_found = _solution_1(root.left, p, q)
    right_has_found = _solution_1(root.right, p, q)
    if ((root == p or root == q) and (left_has_found or right_has_found)) \
        or (left_has_found and right_has_found):
        if ans is not None:
            ans = root
    return left_has_found or right_has_found or root == p or root == q