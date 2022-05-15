
"""
https://leetcode-cn.com/problems/min-stack/
"""
class MinStack:
    """
    两个栈，一个栈存储元素。另一个栈存储最小元素，与第一个栈同步。
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self._min = None


    def push(self, x: int) -> None:
        self.stack1.append(x)
        if self._min is None or x < self._min:
            self._min = x
        self.stack2.append(self._min)


    def pop(self) -> None:
        self.stack2.pop()
        if len(self.stack2) != 0:
            self._min = self.stack2[-1]
        else:
            self._min = None
        return self.stack1.pop()


    def top(self) -> int:
        return self.stack1[-1]


    def min(self) -> int:
        return self.stack2[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()