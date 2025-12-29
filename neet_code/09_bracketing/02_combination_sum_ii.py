"""
Combination Sum II

def combination_sum_ii(nums: List[int], target: int) -> List[List[int]]:

You are given an array of integers candidates, which may contain duplicates, and a target integer target.
Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
Each element from candidates may be chosen at most once within a combination.
The solution set must not contain duplicate combinations.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:
Input: candidates = [9,2,2,4,6,1,5], target = 8
Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]

Example 2:
Input: candidates = [1,2,3,4,5], target = 7
Output: [
  [1,2,4],
  [2,5],
  [3,4]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"candidates": [9,2,2,4,6,1,5], "target": 8}, "output": [[1,2,5],[2,2,4],[2,6]]},
    {"input": {"candidates": [1,2,3,4,5], "target": 7}, "output": [[1,2,4],[2,5],[3,4]]},
]

COMPLEXITY = """
Time                    Complexity
Case	                Complexity	Explanation
Worst case	            O(2ⁿ)	Backtracking explores subsets of candidates
Typical case	        Much less than 2ⁿ	Strong pruning from sorting + candidate > target
Output-sensitive	    Yes	Runtime depends on number of valid combinations

Space Complexity
Component	        Complexity	            Notes
Recursion stack	    O(n)	                Depth ≤ number of candidates
Path storage	    O(n)	                Current combination being built
Output storage	    O(total output size)	Unavoidable, dominates space
"""


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    results: list[list[int]] = []
    path: list[int] = []

    def dfs(idx: int, target_: int) -> None:

        # keep solution if valid
        if target_ == 0:
            results.append(path.copy())
            return

        for i in range(idx, len(candidates)):

            # prune
            if candidates[i] > target_:
                break

            # skip candidat is previous "twin" was not taken
            if i > idx and candidates[i-1] == candidates[i]:
                continue

            # try i'th candidate
            path.append(candidates[i])
            dfs(i + 1, target_ - candidates[i])
            path.pop()

    dfs(0, target)

    return results


function = combination_sum_ii


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
