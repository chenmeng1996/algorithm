"""
https://leetcode-cn.com/problems/string-to-integer-atoi/
"""

def myAtoi(s: str) -> int:
    """
    有限状态机。
    """
    class Automaton:
        def __init__(self) -> None:
            self.table = {
                "start": ["start", "signed", "in_number", "end"],
                "signed": ["end", "end", "in_number", "end"],
                "in_number": ["end", "end", "in_number", "end"],
                "end": ["end", "end", "end", "end"]
            }
            self.state = "start"
            self.signed = 1
            self.res = 0
            self.INT_MAX = 2 ** 31 - 1
            self.INT_MIN = -2 ** 31
        
        def get_index(self, c: str):
            if c == " ":
                return 0
            if c in ["+", "-"]:
                return 1
            if c.isdigit():
                return 2
            # 其他字符
            return 3
        

        def read(self, c: str):
            # 更新当前状态
            self.state = self.table[self.state][self.get_index(c)]
            if self.state in ["start", "end"]:
                return
            # 记录正负号
            if self.state == "signed":
                if c == "-":
                    self.signed = -1 
            # 记录绝对值数字
            else:
                self.res = self.res * 10 + int(c)
                if self.signed * self.res < self.INT_MIN:
                    self.res = self.INT_MAX + 1
                elif self.signed * self.res > self.INT_MAX:
                    self.res = self.INT_MAX
        

        def get_res(self):
            return self.signed * self.res

    automaton = Automaton()
    for v in s:
        automaton.read(v)
    return automaton.get_res()


if __name__  == "__main__":
    res = myAtoi("  -123abc")
    print(res)