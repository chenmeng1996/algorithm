

"""
https://leetcode-cn.com/problems/fraction-to-recurring-decimal/
"""
def fractionToDecimal(numerator: int, denominator: int) -> str:
    """
    长除法，模拟除法运算，记录余数。当出现重复余数时，即出现循环。

    循环例子：821/370
    """
    if numerator == 0:
        return "0"
    res = []
    # 记录负号
    if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
        res.append("-")
    numerator = abs(numerator)
    denominator = abs(denominator)

    # 记录整数
    a = numerator // denominator
    res.append(str(a))
    if numerator != 0:
        res.append(".")
    # 记录小数
    dic = {}
    numerator %= denominator # 求完整数后的第一次余数
    while numerator != 0 and numerator not in dic:
        # 记录余数
        dic[numerator] = len(res)-1
        # 余数乘10，开始计算
        numerator *= 10
        a = numerator // denominator
        res.append(str(a))
        numerator %= denominator
    if numerator != 0:
        index = dic[numerator]
        res.insert(index+1, "(")
        res.append(")")

    return "".join(res)