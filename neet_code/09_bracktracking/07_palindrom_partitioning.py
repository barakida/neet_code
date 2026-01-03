"""
Palindrome Partitioning

def partition(s: str) -> List[List[str]]:

Given a string s, split s into substrings where every substring is a palindrome.
Return all possible lists of palindromic substrings.
You may return the solution in any order.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 20
s contains only lowercase English letters.
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "aab"}, "output": [["a","a","b"],["aa","b"]]},
    {"input": {"s": "a"}, "output": [["a"]]},
]

COMPLEXITY = """
Final complexity:
Time: O(n^2 + n·2^n)
Space: O(n^2 + n·2^n)
"""


def partition(s: str) -> List[List[str]]:
    len_s = len(s)

    # mark palindrome starts in palindrome_matrix (pal_mat)
    # row  is pal_length (pal_length = row + 1) col is position start
    # not that I will mark all words of length 0 are palindromes.
    # this is for code simplicity at the cost of one word length in memory.
    # we will later skip first line.
    pal_mat = [[True] * len_s for _ in range(2)] + [[False] * len_s for _ in range(len_s - 1)]
    for r in range(2, len_s + 1, 1):
        for c in range(0, len_s - r + 1, 1):
            if pal_mat[r - 2][c + 1] and c + r - 1 < len_s and s[c] == s[c + r - 1]:
                pal_mat[r][c] = True

    # init results
    results = []
    path = []


    def dfs(c: int) -> None:
        # save results (if valid)
        if c == len_s:
            results.append(path.copy())
            return

        # try adding palindrome
        for r in range(1, len_s + 1):
            if pal_mat[r][c]:
                path.append(s[c: c + r])
                dfs(c=c + r)
                path.pop()


    # traverse pal_mat to generate wanted results
    dfs(c=0)

    return results


function = partition


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
