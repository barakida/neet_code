"""
Daily Temperatures

def dailyTemperatures(temperatures: List[int]) -> List[int]:

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a
future day.
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [22,21,20]
Output: [0,0,0]

Constraints:
1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"temperatures": [30, 38, 30, 36, 35, 40, 28]}, "output": [1,4,1,2,1,0,0]},
    {"input": {"temperatures": [22, 21, 20]}, "output": [0,0,0]},
]

COMPLEXITY = """
Complexity
Time: O(n) → each index pushed/popped at most once.
Space:O(n) for stack + result.
"""


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    stack = list()  # will store indices

    for i, temp in enumerate(temperatures):
        # if current temp is warmer than temp at stack top
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            result[j] = i - j

        stack.append(i)

    return result


function = dailyTemperatures


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
