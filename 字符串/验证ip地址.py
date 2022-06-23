
"""
https://leetcode-cn.com/problems/validate-ip-address/
"""
def validIPAddress(queryIP: str) -> str:
    count1 = count2 = 0
    for v in queryIP:
        if v == ".":
            count1 += 1
        if v == ":":
            count2 += 1
    if count1 > 0 and count2 > 0:
        return "Neither"
    if count1 > 0 and count1 != 3:
        return "Neither"
    if count2 > 0 and count2 != 7:
        return "Neither"
    
    def validIPv4(queryIP: str):
        arr = queryIP.split(".")
        for v in arr:
            if v == "":
                return False
            if not v.isdigit():
                return False
            if len(v) > 1 and v[0] == "0":
                return False
            if int(v) > 255:
                return False
        return True

    def validIPv6(queryIP: str):
        arr = queryIP.split(":")
        for v in arr:
            if v == "":
                return False
            if len(v) > 4:
                return False
            for c in v:
                if not (("0" <= c and c <= "9") or ("a" <= c and c <= "f") or ("A" <= c and c <= "F")):
                    return False
        return True

    if count1 > 0:
        if validIPv4(queryIP):
            return "IPv4"
        else:
            return "Neither"
    if count2 > 0:
        if validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
    return "Neither"