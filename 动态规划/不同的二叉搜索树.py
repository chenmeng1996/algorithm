
"""
https://leetcode-cn.com/problems/unique-binary-search-trees/
"""
def numTrees(n: int) -> int:
    """
    遍历1-n，将每个数字作为root，左边作为左子树，右边作为右子树。然后递归的计算左子树和右子树的种数。
    设F(i,n)表示长度为n的序列，i作为root时的二叉搜索树的种数。
    设G(n)表示长度为n的序列，二叉搜索树的种数。
    那么有，G(n) = sum(F(i,n)) 1<=i<=n。
    又因为F(i,n)的种数是左子树的种数乘以右子树的种数，所以F(i,n) = G(i-1)*G(n-i)。
    综合两个公式，得到G(n) = sum(G(i-1)*G(n-i)) 1<=i<=n。
    于是，可以用动态规划计算G(n)。
    """
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1]*dp[i-j]
    return dp[n]