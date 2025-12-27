"""
Longest Consecutive Sequence

def longestConsecutive(nums: List[int]) -> int:

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [2, 20, 4, 10, 3, 4, 5]}, "output": 4},
    {"input": {"nums": [0, 3, 2, 5, 4, 6, 1, 1]}, "output": 7},
]


COMPLEXITY = """
Complexity
Time: O(n) average — each element is inserted once and advanced through at most once.
Space: O(n) for the set.
"""


def longestConsecutive(nums: List[int]) -> int:
    # use set for faster search
    values = set(nums)

    # iterate over values
    length = 0
    for current in values:

        # looking only for consecutive chain start
        if current - 1 in values:
            continue

        # count additional links (chain starts with one link)
        next_value = current
        for additional_links in range(1, len(nums) + 1, 1):
            next_value += 1
            if next_value not in values:
                break
        length = max(length, additional_links)

    return length


function = longestConsecutive


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
