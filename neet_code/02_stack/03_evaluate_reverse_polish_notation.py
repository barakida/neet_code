"""
Evaluate Reverse Polish Notation

def evalRPN(tokens: List[str]) -> int:

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"tokens": ["1","2","+","3","*","4","-"]}, "output": 5},
]

COMPLEXITY = """
Time: O(n) — each token processed once.
Space: O(n) — stack worst case holds about n/2 numbers.
"""


def evalRPN(tokens: List[str]) -> int:
    values = list()

    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            assert len(values) >= 2, "!tokens error!"
            v2 = values.pop()
            v1 = values.pop()
        if t == "+":
            t = v1 + v2
        elif t == "-":
            t = v1 - v2
        elif t == "*":
            t = v1 * v2
        elif t == "/":
            t = int(v1 / v2)
        else:
            t = int(t)
        values.append(t)

    return values.pop()


function = evalRPN


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
