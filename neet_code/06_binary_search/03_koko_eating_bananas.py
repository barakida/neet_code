"""
Koko Eating Bananas

def minEatingSpeed(piles: List[int], h: int) -> int:

You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k.
Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas,
you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours.
With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9),
thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25

Constraints:
1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"piles": [1,4,3,2], "h": 9}, "output": 2},
    {"input": {"piles": [25,10,23,4], "h": 4}, "output": 25},
]

COMPLEXITY = """
O(n log max(piles))
"""


def eating_time(piles: List[int], speed: int) -> int:
    return sum((p + speed - 1) // speed for p in piles)


def minEatingSpeed(piles: List[int], h: int) -> int:
    s_min, s_max = 1, max(piles)
    min_speed = s_max
    while s_min <= s_max:
        s = (s_min + s_max) // 2
        t = eating_time(piles=piles, speed=s)
        if t <= h:
            min_speed = min(min_speed, s)
            s_max = s - 1
        else:
            s_min = s + 1

    return min_speed


function = minEatingSpeed


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
