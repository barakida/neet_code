"""
Trapping Rain Water

def trap(height: List[int]) -> int:

You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Constraints:
1 <= height.length <= 1000
0 <= height[i] <= 1000
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"height": [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]}, "output": 9},
]

COMPLEXITY = """
Complexity
Time: O(n) (one pass)
Space: O(1)
"""


def trap(height: List[int]) -> int:
    result, h_i1_max, h_i2_max = 0, 0, 0
    i1, i2 = 0, len(height) - 1

    while i1 < i2:
        h_i1_max = max(h_i1_max, height[i1])
        h_i2_max = max(h_i2_max, height[i2])

        if h_i1_max < h_i2_max:
            result += h_i1_max - height[i1]
            i1 += 1
        else:
            result += h_i2_max - height[i2]
            i2 -= 1

    return result


function = trap


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
