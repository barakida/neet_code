"""
Container With Most Water

def maxArea(heights: List[int]) -> int:

You are given an integer array heights where heights[i] represents the height of the i'th bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"heights": [1, 7, 2, 5, 4, 7, 3, 6]}, "output": 36},
    {"input": {"heights": [2, 2, 2]}, "output": 4},
]

COMPLEXITY = """
Complexity
Time: O(n) — single pass with two pointers.
Space: O(1).
"""


def maxArea(heights: List[int]) -> int:
    max_area = 0
    i1, i2 = 0, len(heights) - 1
    while i1 < i2:
        max_area = max(max_area, min(heights[i1], heights[i2]) * (i2 - i1))
        if heights[i1] < heights[i2]:
            i1 += 1
        else:
            i2 -= 1

    return max_area


function = maxArea


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
