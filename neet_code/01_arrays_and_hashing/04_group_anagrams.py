"""
Group Anagrams

def groupAnagrams(strs: List[str]) -> List[List[str]]:

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from collections import defaultdict
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"strs": ["act", "pots", "tops", "cat", "stop", "hat"]},
     "output": [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]},
    {"input": {"strs": ["x"]}, "output": [["x"]]},
    {"input": {"strs": [""]}, "output": [[""]]},
]

COMPLEXITY = """
Complexity
Time: O(n⋅k) (since counting letters is linear, no sort)
Space: O(n⋅k)
"""


def get_anagram_signature(string: str) -> tuple:
    anagram_vector = [0] * 26  # 26 = len("abcdefghijklmnopqrstuvwxyz")
    for s in string:
        anagram_vector[ord(s) - ord("a")] += 1
    return tuple(anagram_vector)


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    results_map = defaultdict(list)
    for string in strs:
        anagram_signature = get_anagram_signature(string=string)
        results_map[anagram_signature].append(string)

    return list(results_map.values())


function = groupAnagrams


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
