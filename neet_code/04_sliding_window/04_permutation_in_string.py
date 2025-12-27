"""
Permutation in String

def checkInclusion(s1: str, s2: str) -> bool:
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false

Constraints:
1 <= s1.length, s2.length <= 1000
"""

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s1": "abc", "s2": "lecabee"}, "output": True},
    {"input": {"s1": "abc", "s2": "lecaabee"}, "output": False},
]

COMPLEXITY = """
Time: O(∣s1∣+∣s2∣) — single pass with O(1) updates.
Space: O(1) — two arrays of length 26.
"""


def checkInclusion(s1: str, s2: str) -> bool:  # "abcd"
    if len(s2) < len(s1):
        return False
    base = ord("a")

    # prepare vector representatives for target and current
    target, current = [0] * 26, [0] * 26
    for i in range(len(s1)):
        target[ord(s1[i]) - base] += 1
        current[ord(s2[i]) - base] += 1

    # count number of differences between target and current
    misses = sum(t != c for t, c in zip(target, current))
    if misses == 0:
        return True

    # iterate over s2
    for idx_out in range(len(s2) - len(s1)):
        idx_in = idx_out + len(s1)

        # prepare letter idxs
        letter_out_idx = ord(s2[idx_out]) - base
        letter_in_idx = ord(s2[idx_in]) - base

        # update misses
        if current[letter_out_idx] == target[letter_out_idx]:  # current is good and we are changing it
            misses += 1
        if current[letter_in_idx] == target[letter_in_idx]:  # current is good and we are changing it
            misses += 1
        current[letter_out_idx] -= 1                         # update 1
        current[letter_in_idx] += 1                         # update 2
        if current[letter_out_idx] == target[letter_out_idx]:  # update is good
            misses -= 1
        if current[letter_in_idx] == target[letter_in_idx]:  # update is good
            misses -= 1

        # check now status
        if misses == 0:
            return True

    return False


function = checkInclusion


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
