"""
Generate Parentheses

def generateParenthesis(n: int) -> List[str]:

You are given an integer n.
Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:
Input: n = 1
Output: ["()"]

Example 2:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.

Constraints:
1 <= n <= 7
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"n": 1}, "output": ["()"]},
    {"input": {"n": 3}, "output": ["((()))","(()())","(())()","()(())","()()()"]},
]

COMPLEXITY = """
Complexity
Number of valid strings for n = C_n (the n-th Catalan number).
C_n = (1 / (n+1))(2n over n)
Time: O(C_n) — we only generate valid sequences.
Space: O(C_n ⋅ n) — storing all results, recursion depth O(n)
"""


def generateParenthesis(n: int) -> List[str]:
    stack = list()
    results = list()

    # initiate first state in stack
    state = {"string": [], "count_open": 0, "count_close": 0}
    stack.append(state)

    while stack:
        state = stack.pop()

        # deal with finished string
        if state["count_close"] == n:
            results.append(''.join(state["string"]))
            continue

        # if we can still close a bracket
        if state["count_close"] < state["count_open"]:
            new_state = {"string": state["string"] + [")"],
                         "count_open": state["count_open"],
                         "count_close": state["count_close"] + 1}
            stack.append(new_state)

        # if we can still open a bracket
        if state["count_open"] < n:
            new_state = {"string": state["string"] + ["("],
                         "count_open": state["count_open"] + 1,
                         "count_close": state["count_close"]}
            stack.append(new_state)

    return results


function = generateParenthesis


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
