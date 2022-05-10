def sumNums(n: int) -> int:
    def quick_mul(a, b):
        """使用位运算进行乘法"""
        ans = 0
        while b>0:
            if b&1:
                ans += a
            a = a<<1
            b = b>>1
        return ans
    res = quick_mul(1+n, n)
    return res>>1
            

if __name__ == "__main__":             
    sumNums(9)