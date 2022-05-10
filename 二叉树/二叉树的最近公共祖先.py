def solution_1(root: TreeNode, p, q) -> TreeNode: 
    
    def helper(root: TreeNode, p, q, ans) -> bool:
        if root is None:
            return False
        if len(ans) > 0: # 已经得到结果，跳出递归
            return False
        left_has_found = helper(root.left, p, q, ans) # 左子树是否包含p或q
        right_has_found = helper(root.right, p, q, ans) # 右子树是否包含p或q
        if ((root == p or root == q) and (left_has_found or right_has_found)) \
            or (left_has_found and right_has_found):
            if len(ans) == 0:
                ans.append(root)
        return left_has_found or right_has_found or root == p or root == q
    
    ans = []
    helper(root, p, q, ans)
    return ans[0]