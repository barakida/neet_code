"""
House Robber II

def rob(nums: List[int]) -> int:

You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
You are planning to rob money from the houses, but you cannot rob two adjacent houses
because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses.
The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List

EXAMPLES = [
    {"input": {"nums": [3,4,3]}, "output": 4},
    {"input": {"nums": [2,9,8,3,6]}, "output": 15},
]

COMPLEXITY = """
"""


from typing import List

# gpt solution
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    def rob_linear(arr: List[int]) -> int:
        prev2 = prev1 = 0
        for x in arr:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

    return max(
        rob_linear(nums[:-1]),  # exclude last house
        rob_linear(nums[1:])    # exclude first house
    )


function = rob


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()
