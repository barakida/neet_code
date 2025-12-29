"""
Combination Sum

def combination_sum(nums: List[int], target: int) -> List[List[int]]:

You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
The same number may be chosen from nums an unlimited number of times.
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:
Input:
nums = [2,5,6,9]
target = 9
Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:
Input:
nums = [3,4,5]
target = 16
Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
Input:
nums = [3]
target = 5
Output: []

Constraints:
All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [2,5,6,9], "target": 9}, "output": [[2,2,5],[9]]},
    {"input": {"nums": [3,4,5], "target": 16}, "output": [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]},
    {"input": {"nums": [3], "target": 5}, "output": []},
]

COMPLEXITY = """
Aspect	            Complexity
Time	            O(n^(target / min(nums))) (worst-case upper bound)
Stack space	        O(target / min(nums))
Extra space	        O(target / min(nums))
Output space	    O(total number of elements in all combinations)
"""


def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    results: list[list[int]]= []
    path: list[int] = []

    def dfs(idx: int, target_: int):
        if target_ == 0:
            results.append(path.copy())
            return

        for i in range(idx, len(nums)):
            if nums[i] > target_:
                break
            path.append(nums[i])
            dfs(i, target_ - nums[i])
            path.pop()

    dfs(0, target)

    return results


function = combination_sum


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
