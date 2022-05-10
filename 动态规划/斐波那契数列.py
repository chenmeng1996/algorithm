import unittest

"""斐波那契数列"""


def fib1(n):
    """递归，O(N**2)"""
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    """带备忘录的递归，对递归树剪支，O(N)"""
    memo = [0 for i in range(n + 1)]

    def helper(n1):
        if n1 == 1 or n1 == 2:
            memo[n1] = 2
            return 1
        if memo[n1 - 1] == 0:
            memo[n1 - 1] = helper(n1 - 1)
        if memo[n1 - 2] == 0:
            memo[n1 - 2] = helper(n1 - 2)
        return memo[n1 - 1] + memo[n1 - 2]

    return helper(n)


def fib3(n):
    """dp数组，自底向上，非递归，O(N)"""
    dp = [0]
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            dp.append(1)
            continue
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def fib4(n):
    """压缩db数组，因为dp数组实际上每次只用最后两个数"""
    if n == 1 or n == 2:
        return 1
    dp = [0, 0]
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            dp[i - 1] = 1
            continue
        dp_i = dp[0] + dp[1]
        dp[0], dp[1] = dp[1], dp_i
    return dp[1]


class Test(unittest.TestCase):
    def test_fib1(self):
        print(fib1(35))

    def test_fib2(self):
        print(fib2(35))

    def test_fib3(self):
        print(fib3(35))

    def test_fib4(self):
        print(fib4(35))
