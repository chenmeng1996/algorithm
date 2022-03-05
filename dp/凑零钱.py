from typing import List

'''
coins 中是可选硬币面值，amount 是目标金额
f(n)表示amount为n时最少需要的硬币数。
f(n) = min(f(n-a1) + 1, f(n-a2) + 1, ... , f(n-ai) + 1), a1~ai是可选的硬币面值
'''
def coin_change(coins: List[int], amount: int) -> int:
    dp_table = [None for _ in range(amount+1)]
    return coin_change_helper(coins, amount, dp_table)
    
def coin_change_helper(coins: List[int], amount: int, dp_table) -> int:
    if amount == 0:
        return 0
    min_res = None
    for coin in coins:
        if amount < coin:
            continue
        if dp_table[amount - coin] is not None:
            res = dp_table[amount - coin]
        else:
            res = coin_change_helper(coins, amount - coin, dp_table)
            dp_table[amount - coin] = res
        if res == -1:
            continue
        if min_res is None or res + 1 < min_res:
            min_res = res + 1
    if min_res is not None:
        return min_res
    else:
        return -1
        
if __name__ == "__main__":
    res = coin_change([1, 2, 5], 100)
    print(res)