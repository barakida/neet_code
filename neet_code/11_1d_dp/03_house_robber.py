"""
House Robber

def rob(nums: List[int]) -> int:

You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses,
but you cannot rob two adjacent houses because the security system will
automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List

EXAMPLES = [
    {"input": {"nums": [1,1,3,3]}, "output": 4},
    {"input": {"nums": [2,9,8,3,6]}, "output": 16},
]

COMPLEXITY = """
"""


def rob(nums: List[int]) -> int:
    one_back, two_back, three_back = 0, 0, 0
    for num in nums:
        one_back, two_back, three_back = max(two_back, three_back) + num, one_back, two_back

    return max(one_back, two_back)


function = rob


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()
