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
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1,2,3]}, "output": [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]},
    {"input": {"nums": [7]}, "output": [[],[7]]},
]

COMPLEXITY = """

"""


def subsets(nums: List[int]) -> List[List[int]]:
    pass


function = subsets


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
