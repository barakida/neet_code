"""
Products of Array Except Self

def productExceptSelf(nums: List[int]) -> List[int]:

Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1, 2, 4, 6]}, "output": [48, 24, 12, 8]},
    {"input": {"nums": [-1, 0, 1, 2, 3]}, "output": [0, -6, 0, 0, 0]},
]

COMPLEXITY = """
Complexity
Time: O(n) (two passes)
Space: O(1) extra (ignoring output array)
Satisfies follow-up constraint (no division).
"""


def productExceptSelf(nums: List[int]) -> List[int]:
    # init results
    results = [1] * len(nums)

    # forward pass
    factor = 1
    for idx in range(len(nums)):
        results[idx] *= factor
        factor *= nums[idx]

    # backwards pass
    factor = 1
    for idx_ in range(len(nums)):
        idx = len(nums) - 1 - idx_
        results[idx] *= factor
        factor *= nums[idx]

    return results


function = productExceptSelf


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
