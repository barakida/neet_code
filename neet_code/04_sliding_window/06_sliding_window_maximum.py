"""
Sliding Window Maximum

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:

You are given an array of integers nums and an integer k.
There is a sliding window of size k that starts at the left edge of the array.
The window slides one position to the right until it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.

Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

Constraints:
1 <= nums.length <= 1000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
"""

from typing import List
from collections import deque

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1, 2, 1, 0, 4, 2, 6], "k": 3}, "output": [2, 2, 4, 4, 6]},
]

COMPLEXITY = """

"""


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    idx_list = deque()
    results = list()

    for idx, n in enumerate(nums):

        # update idx_list of monotonic decreasing deque
        while idx_list and nums[idx_list[-1]] < n:
            idx_list.pop()
        idx_list.append(idx)

        # remove access values (hold only k "nums" values)
        while idx_list[0] <= idx - k:
            idx_list.popleft()

        # add max value (first idx in idx_list)
        if idx + 1 >= k:
            results.append(nums[idx_list[0]])

    return results


function = maxSlidingWindow


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
