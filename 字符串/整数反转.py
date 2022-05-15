
"""
https://leetcode.cn/problems/reverse-integer/
"""
def reverse(x: int) -> int:
    """
    x转成字符串, 遍历, 每次数字*10累加, 在累加时判断通过 (2**31-1)//10判断是否溢出。
    """
    s = str(x)
    count = 1 / 10
    res = 0
    max_value = 2**31-1
    min_value = -2**31
    if s[0] == "-":
        flag = -1
        s = s[1:]
    else:
        flag = 1
    for c in s:
        if count > max_value // 10:
            return 0
        count *= 10
        c = int(c)
        if c > max_value // count:
            return 0
        if flag == 1 and res > max_value - c * count:
            return 0
        if flag == -1 and -res < min_value + c * count:
            return 0
        res += c * count
    return int(flag * res)


if __name__ == "__main__":
    res = reverse(-123)
    print(res)