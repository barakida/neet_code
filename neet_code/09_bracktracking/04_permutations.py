"""
Permutations

def permute(nums: List[int]) -> List[List[int]]:

Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [7]
Output: [[7]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"nums": [1,2,3]}, "output": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]},
    {"input": {"nums": [7]}, "output": [[7]]},
]

COMPLEXITY = """
Time Complexity
Aspect	                    Complexity	    Explanation
Number of permutations	    n!	            All permutations must be generated
Work per permutation	    O(n)	        Copying path into results
Total time	                O(n · n!)	    Dominated by output construction

Space Complexity
Component	                Complexity	    Notes
Recursion stack	            O(n)	        Depth = permutation length
path list	                O(n)	        Current permutation
used array	                O(n)	        Tracks used indices
Output storage	            O(n · n!)	    All permutations stored
"""


def permute(nums: List[int]) -> List[List[int]]:
    results: list[list[int]] = []
    path: list[int] = []
    used: list[bool] = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            results.append(path.copy())
            return

        for idx in range(len(nums)):
            if used[idx]:
                continue
            used[idx] = True
            path.append(nums[idx])
            dfs()
            path.pop()
            used[idx] = False

    dfs()

    return results


function = permute


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
