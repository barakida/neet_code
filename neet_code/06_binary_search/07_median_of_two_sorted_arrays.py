"""
Median of Two Sorted Arrays

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

You are given two integer arrays nums1 and nums2 of size m and n respectively,
where each is sorted in ascending order.
Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n)) time.

Example 1:
Input: nums1 = [1,2], nums2 = [3]
Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:
Input: nums1 = [1,3], nums2 = [2,4]
Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results


EXAMPLES = [
    {"input": {"nums1": [1, 2], "nums2": [3]}, "output": 2.0},
    {"input": {"nums1": [1, 3], "nums2": [2, 4]}, "output": 2.5},
]

COMPLEXITY = """
O(log(m+n))
"""

# [1, 3], [2, 4]  -> 2.5
# [1, 3, 5], [2, 4]  -> 3
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l1, l2, r1, r2 = 0, 0, len(nums1) - 1, len(nums2) - 1

    d = (len(nums1) + len(nums2) + 1) % 2
    while l1 + d <= r1 or l2 + d <= r2:
        if r1 - l1 > r2 - l2:
            m1 = (l1 + r1) // 2



function = findMedianSortedArrays


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)