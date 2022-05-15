
"""
量级: 十百千万亿
数字: 零一二三四五六七八九

(1) 零在中文数字串中起补位作用，处理的时候可以忽略掉
(2) 一十通常直接缩减为十，意味着十前获取不到数字时为一十
(3) 单位千、百、十前的数为单个数字
(4) 单位万前的数可以由（3）复合而成
(5) 单位亿前的数可以由（3）、（4）及亿本身复合而成



一百二十三万四千五百六十七 -> 1234567
"""
def translate(s: str):
    def _trans(s):
        """最大单位是千的数"""
        num = 0
        if len(s) == 0:
            return 0
        idx_q, idx_b, idx_s = s.find('千'), s.find('百'), s.find('十')
        # 有千，计算千之前的数
        if idx_q != -1:
            num += digit[s[idx_q - 1:idx_q]] * 1000
        # 有百，计算百之前的数
        if idx_b != -1:
            num += digit[s[idx_b - 1:idx_b]] * 100
        # 有十，计算十之前的数
        if idx_s != -1:
            # 十前忽略一的处理
            num += digit.get(s[idx_s - 1:idx_s], 1) * 10
        # 计算个位数
        if s[-1] in digit:
            num += digit[s[-1]]
        return num

    digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    s = s.replace("零", "")
    # 寻找最后一个亿和万出现的位置，即代表亿和万单位的位置
    idx_y, idx_w = s.rfind('亿'), s.rfind('万')
    if idx_w < idx_y:
        idx_w = -1
    num_y, num_w = 100000000, 10000
    # 有亿，有万，则分别求 亿之前的数 和 万之前的数 和 万之后的数
    if idx_y != -1 and idx_w != -1:
        return translate(s[:idx_y]) * num_y + _trans(s[idx_y + 1:idx_w]) * num_w + _trans(s[idx_w + 1:])
    # 只有亿，则分别求 亿之前的数 和 万之后的数
    elif idx_y != -1:
        return translate(s[:idx_y]) * num_y + _trans(s[idx_y + 1:])
    # 只有万，则分别求 万之前的数 和 万之后的数
    elif idx_w != -1:
        return _trans(s[:idx_w]) * num_w + _trans(s[idx_w + 1:])
    # 没有亿和万，则直接求万之后的数
    return _trans(s)
