"""
Coin Change

def coin_change(coins: List[int], amount: int) -> int:

You are given an integer array coins representing coins of different denominations
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1.
You may assume that you have an unlimited number of each coin.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:
1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000
"""
from typing import List

COMPLEXITY = """
Complexity
Solution	        Time	    Space
DP (bottom-up)	    O(A·C)	    O(A)
"""

EXAMPLES = [
    {"input": {"coins": [1,5,10], "amount": 12}, "output": 3},
    {"input": {"coins": [2], "amount": 3}, "output": -1},
    {"input": {"coins": [1], "amount": 0}, "output": 0},
]

def coin_change(coins: List[int], amount: int) -> int:
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for idx in range(1, len(dp)):
        for c in coins:
            if c <= idx and dp[idx - c] != INF:
                dp[idx] = min(dp[idx], dp[idx - c] + 1)

    return dp[-1] if dp[-1] != INF else -1


function = coin_change


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()

