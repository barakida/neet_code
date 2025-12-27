"""
Find the Duplicate Number
def findDuplicate(nums: List[int]) -> int:

You are given an array of integers nums containing n + 1 integers.
Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer which appears two or more times.
Return the integer that appears more than once.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

Constraints:
1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"nums": [1, 2, 3, 2, 2]}, "output": 2},
    {"input": {"nums": [1, 2, 3, 4, 4]}, "output": 4},
]

COMPLEXITY = """
Complexity
O(n) time, O(1) extra space
"""


def findDuplicate(nums: list[int]) -> int:

    fast, slow1 = nums[0], nums[0]
    while True:
        fast = nums[nums[fast]]
        slow1 = nums[slow1]
        if fast == slow1:
            break

    slow2 = nums[0]
    while slow1 != slow2:
        slow1, slow2 = nums[slow1], nums[slow2]

    return slow1


function = findDuplicate


if __name__ == '__main__':
    [print(f'expected results: {e["output"]}  |  actual results: {function(**e["input"])}') for e in EXAMPLES]
