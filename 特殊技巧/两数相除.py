
# 快速逼近
def divide(dividend: int, divisor: int) -> int:
    def div(dividend, divisor):
        if dividend < divisor:
            return 0
        count = 1
        tmp_divisor = divisor
        while (tmp_divisor + tmp_divisor) < dividend:
            tmp_divisor = tmp_divisor + tmp_divisor # 除数翻倍
            count = count + count # 商翻倍
        return count + div(dividend - tmp_divisor, divisor)

    if dividend == 0:
        return 0
    if divisor == 0:
        raise ArithmeticError('divisor cannot be 0')

    # 为了通过测试用例，模拟了C++和Java中的int类型最小值
    MIN_INT = -(1 << 31)
    if dividend == MIN_INT and divisor == -1:
        return -MIN_INT - 1

    if divisor == 1 or divisor == -1:
        return dividend * divisor
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    else:
        sign = 1
    return sign * div(abs(dividend), abs(divisor))

if __name__ == '__main__':
    res = divide(10, 3)
    print(res)


    
