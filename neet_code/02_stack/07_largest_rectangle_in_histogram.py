"""
Largest Rectangle In Histogram

def largestRectangleArea(heights: List[int]) -> int:

You are given an array of integers heights where heights[i] represents the height of a bar.
The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 1000.
0 <= heights[i] <= 1000
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"heights": [7, 1, 7, 2, 2, 4]}, "output": 8},
    {"input": {"heights": [1, 3, 7]}, "output": 7},
]

COMPLEXITY = """
Complexity
Time: O(n) (each index pushed/popped once)
Space: O(n) for the stack
"""


def largestRectangleArea(heights: List[int]) -> int:
    stack = list()  # holding index

    area_max = 0
    for idx, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = idx - 1 - (stack[-1] if stack else -1)
            area_max = max(area_max, height * width)
        stack.append(idx)

    return area_max


function = largestRectangleArea


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
