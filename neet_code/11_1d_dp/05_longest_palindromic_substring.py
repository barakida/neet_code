"""
Longest Palindromic Substring

def longest_palindrome(s: str) -> str:

Given a string s, return the longest substring of s that is a palindrome.
A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:
Input: s = "abbc"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s contains only digits and English letters.
"""
COMPLEXITY = """
Complexity
Approach	    Time	Space	Notes
Your solution	O(n²)	O(1)	Optimal practical solution
"""

EXAMPLES = [
    {"input": {"s": "ababd"}, "output": "bab"},
    {"input": {"s": "abbc"}, "output": "bb"},
]

def longest_palindrome(s: str) -> str:
    len_s = len(s)
    best_idx, best_length = 0, 0

    def expand_palindrome(idx: int, length: int) -> None:
        nonlocal len_s, best_idx, best_length

        is_palindrome = True
        while is_palindrome:

            if length > best_length:
                best_length = length
                best_idx = idx

            length += 2
            i1 = idx - length // 2
            i2 = i1 + length - 1
            is_palindrome = 0 <= i1 and i2 < len_s and s[i1] == s[i2]

    for idx in range(len_s):
        expand_palindrome(idx=idx, length=0)
        expand_palindrome(idx=idx, length=1)

    i1 = best_idx - best_length // 2
    i2 = i1 + best_length

    return s[i1:i2]


function = longest_palindrome


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()