
"""
两个长度为m的无序数组A,B 对于任意不相交的两个区间ab和cd
求数组A的两个区间和 减去 数组B的两个区间和最大。
"""
def fn():
    """
    这道题是 连续子数组最大和 的改编。
    可以将数组A的对应元素减去数组B的对应元素, 得到一个新数组.
    求新数组的连续子数组最小和, 则该连续区域之外, 有两个区域, 并且和是最大的。
    所以答案是: 新数组的数组和 - 新数组的连续子数组最小和。
    """
    print(1)

fn()