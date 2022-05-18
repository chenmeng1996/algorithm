

"""
https://leetcode.cn/problems/rectangle-area/
"""
def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    """
    通过两个矩形在x轴和y轴上的投影重合, 来计算重合面积。
    """
    s1 = (ax2-ax1)*(ay2-ay1)
    s2 = (bx2-bx1)*(by2-by1)

    x = max(min(ax2, bx2) - max(ax1, bx1), 0)
    y = max(min(ay2, by2) - max(ay1, by1), 0)

    return s1 + s2 - x * y