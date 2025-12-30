"""
Subsets II

def subsets_with_dup(nums: List[int]) -> List[List[int]]:

You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,1]
Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:
Input: nums = [7,7]
Output: [[],[7], [7,7]]

Constraints:
1 <= nums.length <= 11
-20 <= nums[i] <= 20
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1,2,1]}, "output": [[],[1],[1,2],[1,1],[1,2,1],[2]]},
    {"input": {"nums": [7,7]}, "output": [[],[7], [7,7]]},
]

COMPLEXITY = """
Let: n = len(nums) (n ≤ 11)

Time Complexity
Aspect	                Complexity	                Explanation
Total subsets (max)	    2ⁿ	                        Each element included or excluded
Duplicate pruning	    Reduces constant factor	    Does not change worst-case
Total time	            O(2ⁿ · n)	                Copying each subset costs up to O(n)

Space Complexity
Component	            Complexity	    Notes
Recursion stack	        O(n)	        One level per element
Path list	            O(n)	        Current subset
Output storage	        O(2ⁿ · n)	    All subsets stored
"""


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    results: list[list[int]] = []
    path: list[int] = []

    def dfs(idx: int):

        if idx == len(nums):
            results.append(path.copy())
            return

        dfs(idx + 1)

        if (idx > 0 and nums[idx - 1] == nums[idx]) and (not path or path[-1] != nums[idx]):
            return

        path.append(nums[idx])
        dfs(idx + 1)
        path.pop()


    dfs(0)

    return results


function = subsets_with_dup


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)


"""
GPT Solution

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    results = []
    path = []

    def dfs(start: int):
        results.append(path.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return results
"""