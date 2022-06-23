
"""
https://leetcode.cn/problems/qiu-12n-lcof/

要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句
"""

def sumNums(n: int) -> int:
    """
    递归。逻辑运算符代替if
    """
    n > 0 and sumNums(n-1)
    return n 

def sumNums(n: int) -> int:
    def quick_mul(a, b):
        """
        使用位运算进行乘法。
        然后用等差数列求和公式计算。
        """
        ans = 0
        while b>0:
            if b&1:
                ans += a
            a = a<<1
            b = b>>1
        return ans
    # n*(1+n)
    res = quick_mul(1+n, n)
    # res / 2
    return res>>1
            

if __name__ == "__main__":             
    sumNums(9)