from typing import List

"""
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
"""
def verifyPostorder(postorder: List[int]) -> bool:
    """
    后续遍历的最后一个是根节点，除了根节点，左右分别是左子树和右子树的元素。
    左子树的元素小于根节点，右子树的元素大于根节点。
    递归的检查左子树和右子树。
    """
    def helper(postorder, start, end):
        if start >= end:
            return True
        root = postorder[end]
        # 找出左子树和右子树的分界线
        target = end
        for i in range(end-1, start-1, -1):
            if postorder[i] > root:
                target = i
            else:
                break
        # 检查左子树是否都小于root
        for i in range(start, target):
            if postorder[i] > root:
                return False
        return helper(postorder, start, target-1) and helper(postorder, target, end-1)
    
    return helper(postorder, 0, len(postorder)-1)