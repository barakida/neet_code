"""
Two Sum
Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input:
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [3, 4, 5, 6], "target": 7}, "output": [0, 1]},
    {"input": {"nums": [4, 5, 6], "target": 10}, "output": [0, 2]},
    {"input": {"nums": [5, 5], "target": 10}, "output": [0, 1]},
]

COMPLEXITY = """
Complexity
Time: O(n) → each lookup/insert in hashmap is (O(1) average).
Space: O(n) → hashmap may store all numbers.
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    values_map = dict()
    for idy, num in enumerate(nums):
        idx = values_map.get(num, -1)
        if idx >= 0:
            return [idx, idy]
        values_map[target - num] = idy

    assert False, "twoSum Failed"


function = twoSum


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)

