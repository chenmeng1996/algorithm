

"""
https://leetcode-cn.com/problems/remove-k-digits/
"""
def removeKdigits(num: str, k: int) -> str:
    """
    贪心 + 单调栈

    每去除一个数字，都使得去除后的数字是最小的。
    如果想让去除后的数字最小，应该从高位往低位判断。如果高位比下一个地位大，应该删除高位。如果没有找到（即数字升序），则删除最后一位。

    如果直接删除数组元素，并重复遍历，时间复杂度高，会超时。因此使用单调递增栈。
    """
    stack = []
    for v in num:
        while stack and v < stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(v)

    # 栈内元素递增，如果k大于0，则从后往前删除元素
    while stack and k > 0:
        stack.pop()
        k -= 1
        
    new_num = "".join(stack)
    if len(new_num) == 0:
        return "0"
    return str(int(new_num))