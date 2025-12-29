"""
Subsets

def subsets(nums: List[int]) -> List[List[int]]:

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from collections import deque
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1,2,3]}, "output": [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]},
    {"input": {"nums": [7]}, "output": [[],[7]]},
]

COMPLEXITY = """
Complexity
Let n = len(nums).
Number of subsets: 2^n

Time: O(n * 2^n)
(each subset copy r + [x] costs up to O(n) across the process)

Space: O(2^n) for storing all subsets (and their contents)

This is optimal for a problem that must output 2^n subsets.
"""


def subsets(nums):
    res = [[]]
    for x in nums:
        res += [r + [x] for r in res]
    return res


function = subsets


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
