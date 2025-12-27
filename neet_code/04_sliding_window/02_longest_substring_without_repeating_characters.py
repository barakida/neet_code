"""
Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s: str) -> int:

Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "zxyzxyz"}, "output": 3},
    {"input": {"s": "xxxx"}, "output": 1},
]

COMPLEXITY = """

"""


def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    letter_idx = dict[str, int] = dict()
    i1 = 0

    # iterate over string s
    for i2, l in enumerate(s):

        # update substring start
        if i2 in letter_idx and letter_idx[l] > i1:
            i1 = letter_idx[l] + 1

        # update letter last occurrence
        letter_idx[l] = i2

        # update max length
        max_length = max(max_length, i2 - i1 + 1)

    return max_length


function = lengthOfLongestSubstring


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
