"""
Minimum Window Substring

def minWindow(s: str, t: str) -> str:

Given two strings s and t, return the shortest substring of s such that every character in t,
including duplicates, is present in the substring.
If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""

Constraints:
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""
from collections import Counter, defaultdict

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "OUZODYXAZV", "t": "XYZ"}, "output": "YXAZ"},
    {"input": {"s": "xyz", "t": "xyz"}, "output": "xyz"},
    {"input": {"s": "x", "t": "xy"}, "output": ""},
]

COMPLEXITY = """
Complexity
Time: O(∣s∣+∣t∣) — each index moves at most once.
Space: O(k) — number of distinct letters (≤ 52 for upper/lowercase).
"""


def minWindow(s: str, t: str) -> str:
    if not t or not s or len(t) > len(s):
        return ""

    best_i1 = best_i2 = 0
    target = Counter(t)
    misses = len(target)
    current = defaultdict(int)

    i1 = i2 = 0
    # while i1 <= i2 and i2 < len(s):
    while i2 < len(s) and i1 + misses <= len(s) and i1 + (best_i2 - best_i1) <= len(s):

        # advance i2 to get misses = 0 (then once more)
        while i2 < len(s) and misses:
            if s[i2] in target:
                current[s[i2]] += 1
                if current[s[i2]] == target[s[i2]]:
                    misses -= 1
            i2 += 1

        # advance i1 to get minWindow (then once more)
        while misses == 0:
            if s[i1] in target:
                if current[s[i1]] == target[s[i1]]:  # are we in minWindow?
                    if best_i2 == 0 or best_i2 - best_i1 > i2 - i1:
                        best_i1, best_i2 = i1, i2
                    misses += 1
                current[s[i1]] -= 1
            i1 += 1

    return s[best_i1: best_i2]


function = minWindow


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
