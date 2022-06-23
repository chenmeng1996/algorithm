"""
给一组数据：
Cindy Jason
Alice Jane
Jason Jane
Bob Robert
Jane Jack
Andy Jack
Robert Jack 
表示右边的人是左边的人的上级，给两个名字，找出离他们最近的公共上级。
（我一开始以为是二叉树求公共祖先，结果面试官告诉我是相交链表）
"""

def find_first_intersection(name_tuples, name1, name2):
    dic = {}
    for name_tuple in name_tuples:
        dic[name_tuple[0]] = [name_tuple[0], name_tuple[1]]
    for _, link in dic.items():
        while True:
            boss = link[-1]
            if boss not in dic:
                break
            link.extend(dic[boss][1:])
    link1 = dic[name1]
    link2 = dic[name2]
    if len(link1) == len(link2):
        return link1[-1]
    i = 0
    j = 0
    if len(link1) < len(link2):
        for _ in range(len(link2)-len(link1)):
            j += 1
    if len(link1) > len(link2):
        for _ in range(len(link1)-len(link2)):
            i += 1
    while i < len(link1):
        if link1[i] == link2[j]:
            return link1[i]
        i += 1
        j += 1


if __name__ == "__main__":
    res = find_first_intersection([
        ("Cindy", "Jason"),
        ("Alice", "Jane"),
        ("Jason", "Jane"),
        ("Bob", "Robert"),
        ("Jane", "Jack"),
        ("Andy", "Jack"),
        ("Robert", "Jack")], "Alice", "Bob")
    print(res)