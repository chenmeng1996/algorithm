
from typing import List

"""
https://leetcode-cn.com/problems/gray-code/
"""
def grayCode(n: int) -> List[int]:
    """
    镜像拼接。

    从n=2的格雷码开始推理。
    n=2的其中格雷码一个是[00,01,11,10]。
    那么n=3时，格雷码元素个数是n=2的两倍，首先将n=2的格雷码前面补0，得到n=3格雷码的前一半[000,001,011,010]，这一半满足格雷码定义。
    再将前一半的格雷码的第一位从0改成1，得到[100,101,111,110]，也满足格雷码定义。但前后连接处、首尾不满足格雷码定义。
    所以将后一半逆序，得到[110,111,101,100]。然后将前后拼接，得到n=3的格雷码。
    依次类推，得到任意n的格雷码。
    """
    ans = [0]
    for i in range(1, n + 1):
        for j in range(len(ans) - 1, -1, -1):
            # 倒序，将数字的二进制头部增加1（通过原数字与）
            ans.append(ans[j] | (1 << (i - 1)))
    return ans


if __name__ == "__main__":
    res = grayCode(2)
    print(res)