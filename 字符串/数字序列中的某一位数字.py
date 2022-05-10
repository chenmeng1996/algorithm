
"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。
"""
def findNthDigit(n: int) -> int:
    """
    0~9 10个数字
    10~99 10*2*9个数字
    100~999 100*3*9个数字
    所以x位数的数字个数= 10**(x-1)*x*9, x>1

    先找到第n个数字所在的位数x，再寻找在哪个具体数字。
    """
    if n <= 9:
        return n
    n -= 9
    length = 2
    while True:
        a = 10**(length-1) * length * 9
        if n > a:
            n -= a
            length += 1
        else:
            break
    offset = n // length
    limit = n % length
    start = int("1"+"0"*(length-1))
    if limit == 0:
        return int(str(start + offset - 1)[-1])
    else:
        return int(str(start + offset)[limit-1])