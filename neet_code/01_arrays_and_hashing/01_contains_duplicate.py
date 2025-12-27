"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1, 2, 3, 3]}, "output": True},
    {"input": {"nums": [1, 2, 3, 4]}, "output": False},
]

COMPLEXITY = """
Complexity

Time: O(n) 
Each insertion/lookup in a hash set is 
O(1) average, and we process n elements.

Space: O(n)
In worst case (all elements unique), the set stores all n numbers.

Alternative Solutions

Sorting approach: Sort the list (O(nlogn)), then scan once to check if any two consecutive elements are equal. 
Uses less extra space (O(1) or O(logn)) but slower.

Brute force: Compare every pair → not efficient.
"""


def hasDuplicate(nums: List[int]) -> bool:
    values = set()
    for value in nums:
        if value in values:
            return True
        values.add(value)
    return False


function = hasDuplicate


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
