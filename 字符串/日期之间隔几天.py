
"""
https://leetcode-cn.com/problems/number-of-days-between-two-dates/
"""
def daysBetweenDates(date1: str, date2: str) -> int:
    """
    选择一个很早的日期作为基准，例如1970年1月1日。
    计算两个日期距离基准过去的天数，然后相减即可。

    注意闰年和闰月（闰年的2月是29天）。
    """
    month_map = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def is_special(year):
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True

    def date_to_day(year, month, day):
        res = 0
        for i in range(1970, year):
            if is_special(i):
                res += 366
            else:
                res += 365
        for i in range(1, month):
            if i == 2:
                if is_special(year):
                    res += 29
                else:
                    res += 28
            else:
                res += month_map[i]
        res += day
        return res
    
    d1 = [int(v) for v in date1.split("-")]
    d2 = [int(v) for v in date2.split("-")]
    day1 = date_to_day(d1[0], d1[1], d1[2])
    day2 = date_to_day(d2[0], d2[1], d2[2])
    return max(day1, day2) - min(day1, day2)
    

if __name__ == "__main__":
    res = daysBetweenDates("2020-01-15", "2019-12-31")
    print(res)