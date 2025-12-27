"""
Longest Repeating Character Replacement

def characterReplacement(s: str, k: int) -> int:

You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements,
return the length of the longest substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

Constraints:
1 <= s.length <= 1000
0 <= k <= s.length
"""
from collections import defaultdict

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "XYYX", "k": 2}, "output": 4},
    {"input": {"s": "AAABABB", "k": 1}, "output": 5},
    {"input": {"s": "DDDDDCCABABABABABABABABABABABACCCCCC", "k": 2}, "output": 8},  # example by I.B.
]

COMPLEXITY = """
Complexity
Time: O(n)
Space: O(1) (counts over 26 uppercase letters)
"""


def characterReplacement(s: str, k: int) -> int:
    longest_substring = 0
    counts = defaultdict(int)
    max_frequency = 0

    i1 = 0
    for i2, ch in enumerate(s):
        counts[ch] += 1
        max_frequency = max(max_frequency, counts[ch])
        while (i2 - i1 + 1) - max_frequency > k:
            counts[s[i1]] -= 1
            i1 += 1

        longest_substring = max(longest_substring, i2 - i1 + 1)

    return longest_substring


function = characterReplacement


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
