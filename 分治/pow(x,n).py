"""
https://leetcode-cn.com/problems/powx-n/

快速幂乘法
"""
def myPow(self, x: float, n: int) -> float:
    def quickMul(N):
        if N == 0:
            return 1.0
        y = quickMul(N // 2)
        if N % 2 == 0:
            return y * y
        else:
            return y * y * x

    if n >= 0:
        return quickMul(n)
    else:
        return 1.0 / quickMul(-n)