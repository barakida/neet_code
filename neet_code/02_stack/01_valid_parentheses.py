"""
Valid Parentheses

def isValid(s: str) -> bool:

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
-  Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""
from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"s": "[]"}, "output": True},
    {"input": {"s": "([{}])"}, "output": True},
    {"input": {"s": "[(])"}, "output": False},
]

COMPLEXITY = """
Complexity
Time: O(n) — one pass through the string.
Space: O(n) — worst case, all opens on stack.
"""


def isValid(s: str) -> bool:
    open_close_map = {"{": "}", "(": ")", "[": "]"}

    stack = list()
    for l in s:
        if l in open_close_map.keys():
            stack.append(l)
        else:  # l is a closer
            if len(stack) and open_close_map[stack[-1]] == l:
                stack.pop()
            else:
                return False

    return len(stack) == 0


function = isValid


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
