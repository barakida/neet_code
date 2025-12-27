"""
Top K Frequent Elements

def topKFrequent(nums: List[int], k: int) -> List[int]:

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1, 2, 2, 3, 3, 3], "k": 2}, "output": [2,3]},
    {"input": {"nums": [7, 7], "k": 1}, "output": [7]},
]

COMPLEXITY = """
Complexity
Time: O(n) — counting + linear bucket scan
Space: O(n) — buckets + counter
"""


def topKFrequent(nums: List[int], k: int) -> List[int]:

    # count number frequency
    frequency = dict()
    for n in nums:
        frequency[n] = frequency.get(n, 0) + 1

    # group numbers by frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    [buckets[v - 1].append(k) for k, v in frequency.items()]

    # traverse buckets
    results = list()
    for idx in range(len(buckets)):
        counts = len(buckets) - idx
        if not len(buckets[counts - 1]):
            continue
        results.extend(buckets[counts - 1])
        if len(results) >= k:
            break

    return results


function = topKFrequent


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
