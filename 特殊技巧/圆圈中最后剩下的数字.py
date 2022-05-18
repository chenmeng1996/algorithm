

"""
https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

约瑟夫环问题。
0,1,···,n-1这n个数字排成一个圆圈。
从数字0开始, 每次从这个圆圈里删除第m个数字(删除后从下一个数字开始计数)。
求出这个圆圈里剩下的最后一个数字。
"""
import sys


sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n