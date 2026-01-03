"""
Letter Combinations of a Phone Number

def letter_combinations(digits: str) -> List[str]:

You are given a string digits made up of digits from 2 through 9 inclusive.
Each digit (not including 1) is mapped to a set of characters as shown below:
A digit could represent any one of the characters it maps to.
Return all possible letter combinations that digits could represent. You may return the answer in any order.

digits_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

Example 1:
Input: digits = "34"
Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

Example 2:
Input: digits = ""
Output: []

Constraints:
0 <= digits.length <= 4
2 <= digits[i] <= 9
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"digits": "34"}, "output": ["dg","dh","di","eg","eh","ei","fg","fh","fi"]},
    {"input": {"digits": ""}, "output": []},
]

COMPLEXITY = """
Final complexities:
Time: O(n · k^n) (worst case O(n · 4^n))
Space: O(n · k^n)
"""

digits_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def letter_combinations(digits: str) -> List[str]:
    results = []
    path = []

    def dfs(i: int) -> None:
        if i == len(digits):
            results.append("".join(path))
            return

        for l in digits_map[digits[i]]:
            path.append(l)
            dfs(i + 1)
            path.pop()

    if digits:
        dfs(0)

    return results


function = letter_combinations


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
