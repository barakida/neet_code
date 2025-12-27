"""
Best Time to Buy and Sell Stock

def maxProfit(prices: List[int]) -> int:

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve.
You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"prices": [10, 1, 5, 6, 7, 1]}, "output": 6},
    {"input": {"prices": [10, 8, 7, 5, 2]}, "output": 0},
]

COMPLEXITY = """
Complexity
Time: O(n), single scan.
Space: O(1).
"""


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit


function = maxProfit


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
