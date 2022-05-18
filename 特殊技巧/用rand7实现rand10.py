


def rand7():
    pass

"""
https://leetcode.cn/problems/implement-rand10-using-rand7/
"""
def rand10() -> int:
    """
    使用rand7生成等概率的10个数, 然后映射到1到10。

    使用rand7随机2次, 随机生成一个7进制的数(所有数是等概率的)s。
    """
    while True:
        # 生成2位数的7进制数，并转换成10进制
        # 10进制数的范围是[0, 49]
        # 这些10进制数的概率是相同的，取[0, 9]映射到[1, 10]，其他的数拒绝并重试即可。
        # 为了减少拒绝次数, 尽可能将更多的数映射到[1, 10]。
        # 可以通过将[1, 40] % 10 + 1, 将[1, 40]映射到[1, 10]。
        res = (rand7()-1)*7 + (rand7() - 1)
        if res >= 1 and res <= 40:
            return res % 10 + 1