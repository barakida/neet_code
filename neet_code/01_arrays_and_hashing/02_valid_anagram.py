"""
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""
from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "racecar", "t": "carrace"}, "output": True},
    {"input": {"s": "jar", "t": "jam"}, "output": False},
]

COMPLEXITY = """
Complexity
Time:  O(n) → where n is the length of the strings (we scan each once).
Space: O(1) → since we only store counts for lowercase English letters (fixed alphabet size = 26).
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counts, t_counts = dict(), dict()
    for ls, lt in zip(s, t):
        s_counts[ls] = s_counts.get(ls, 0) + 1
        t_counts[lt] = t_counts.get(lt, 0) + 1

    return s_counts == t_counts


function = isAnagram


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
