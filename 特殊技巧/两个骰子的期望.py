
"""
给定两个骰子，每次扔出去后选择较大的作为当前的值，这个值的期望。
"""
def ex():
    res = 0
    for i in range(1, 7):
        res += (1/6)**2 * ((i-1)*2+1) * i
    return res


if __name__ == "__main__":
    print(ex())