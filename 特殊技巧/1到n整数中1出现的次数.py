
"""
https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
https://leetcode.cn/problems/number-of-digit-one/
"""
def countDigitOne(n: int) -> int:
    """
    思路是遍历数字n的每一位, 把当前位固定为1, 然后转动其他位, 看看有多少种情况。
    当前位有以下几种情况:
    1. cur = 0。
        count = 高位数字 * 当前位因子
    2. cur = 1
        count = 高位数字 * 当前位因子 + 地位数字 + 1
    3. cur > 1
        count = (高位数字 + 1) * 当前位因子

    设数字n是个x位数, 可以写成nxnx-1...n2n1。
    ni为当前位, 设为cur。
    nxnx-1...ni+1是高位, ni-1ni-2...n1是地位。
    10^i是位因子, 设为digit。


    时间复杂度: 循环次数为数字n的位数, 也就是log10n, 所以是O(logn)。
    空间复杂度: O(1)
    """
    digit, res = 1, 0
    high, cur, low = n // 10, n % 10, 0

    # 当 high 和 cur 同时为 0 时，说明已经越过最高位，因此跳出
    while high != 0 or cur != 0:
        if cur == 0: 
            res += high * digit
        elif cur == 1: 
            res += high * digit + low + 1
        else: 
            res += (high + 1) * digit
        # 将 cur 加入 low ，组成下轮 low
        low += cur * digit
        # 下轮 cur 是本轮 high 的最低位
        cur = high % 10
        # 将本轮 high 最低位删除，得到下轮 high
        high //= 10
        digit *= 10
    return res