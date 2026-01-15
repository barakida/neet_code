"""
Palindromic Substrings

def count_substrings(s: str) -> int:

Given a string s, return the number of substrings within s that are palindromes.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

COMPLEXITY = """
Complexity
Approach	    Time	Space	Notes
Your solution	O(n²)	O(1)	Optimal practical solution
"""

EXAMPLES = [
    {"input": {"s": "abc"}, "output": 3},
    {"input": {"s": "aaa"}, "output": 6},
]


def count_substrings(s: str) -> int:
    count = 0
    len_s = len(s)

    def expand_palindrome(i1: int, i2: int) -> None:
        nonlocal count

        while 0 <= i1 and i2 < len_s and s[i1] == s[i2]:
            count += 1
            i1, i2 = i1 - 1, i2 + 1

    for idx in range(len_s):
        expand_palindrome(idx, idx)
    for idx in range(len_s - 1):
        expand_palindrome(idx, idx + 1)

    return count


function = count_substrings


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()
