"""
Valid Palindrome

def isPalindrome(s: str) -> bool:

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "Was it a car or a cat I saw?"}, "output": True},
    {"input": {"s": "tab a cat"}, "output": False},
]

COMPLEXITY = """
Complexity
Time:  O(n), where n=len(s). Each character processed once.
Space: O(1), just pointers (no extra storage).
"""


def isPalindrome(s: str) -> bool:

    # set indexes to string ends
    i1, i2 = 0, len(s) - 1
    while i1 < i2:

        # skip none alphanumeric characters (on the left)
        while i1 < i2 and not s[i1].isalnum():
            i1 += 1

        # skip none alphanumeric characters (on the right)
        while i1 < i2 and not s[i2].isalnum():
            i2 -= 1

        # compare characters
        if s[i1].lower() != s[i2].lower():
            return False

        # advance indexes
        i1 += 1
        i2 -= 1

    return True


function = isPalindrome


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
