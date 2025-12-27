"""
3Sum

def threeSum(nums: List[int]) -> List[List[int]]:

Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [-2, -2, -2, -1, -1, -1, 3, 3, 3, 4, 4, 4]}, "output": [[-2, -2, 4], [-2, -1, 3]]},
    {"input": {"nums": [-1, 0, 1, 2, -1, -4]}, "output": [[-1, -1, 2], [-1, 0, 1]]},
    {"input": {"nums": [0, 1, 1]}, "output": []},
    {"input": {"nums": [0, 0, 0]}, "output": [[0, 0, 0]]},
]

COMPLEXITY = """
Complexity
Time: Sorting O(nlogn) + two-pointer scan per i (O(n^2) total).
Space: O(1) extra (ignoring output).
"""


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    results = list()

    i1 = 0
    while i1 <= n - 3 and nums[i1] <= 0:
        i2, i3 = i1 + 1, n - 1

        # test i2, i3 variants (given i1)
        while i2 < i3:
            s = nums[i1] + nums[i2] + nums[i3]
            if s < 0:
                # advance i2 skipping duplicates
                temp = nums[i2]
                while nums[i2] == temp and i2 < i3:
                    i2 += 1
            elif s > 0:
                # advance i3 skipping duplicates
                temp = nums[i3]
                while nums[i3] == temp and i2 < i3:
                    i3 -= 1
            else:  # s == 0
                # save result
                results.append([nums[i1], nums[i2], nums[i3]])

                # advance i2 skipping duplicates
                temp = nums[i2]
                while nums[i2] == temp and i2 < i3:
                    i2 += 1

                # advance i3 skipping duplicates
                temp = nums[i3]
                while nums[i3] == temp and i2 < i3:
                    i3 -= 1

        # advance i1 skipping duplicates
        temp = nums[i1]
        while nums[i1] == temp and i1 < n - 2:
            i1 += 1

    return results


function = threeSum


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
