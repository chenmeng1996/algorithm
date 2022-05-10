"""
https://leetcode-cn.com/problems/excel-sheet-column-title/
"""
def convertToTitle(columnNumber: int) -> str:
    """
    从1到26的26进制转换。
    因为是从1开始的，我们每次columnNumber减去1，再对26取模，这样会得到一个0到25的数字，0代表A，25代表Z。
    """
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        x = columnNumber % 26
        columnNumber //= 26
        res.append(chr(ord("A") + x))
    res.reverse()
    return "".join(res)
