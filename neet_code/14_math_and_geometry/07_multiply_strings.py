"""
Multiply Strings

def multiply(num1: str, num2: str) -> str:

You are given two strings num1 and num2 that represent non-negative integers.
Return the product of num1 and num2 in the form of a string.
Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.
Note: You can not use any built-in library to convert the inputs directly into integers.

Example 1:
Input: num1 = "3", num2 = "4"
Output: "12"

Example 2:
Input: num1 = "111", num2 = "222"
Output: "24642"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
"""

EXAMPLES = [
    {"input": {"num1": "3", "num2": "4"}, "output": "12"},
    {"input": {"num1": "111", "num2": "222"}, "output": "24642"},
]

COMPLEXITY = """
"""


def multiply(num1: str, num2: str) -> str:
    pass
    """
    see gpt solution bellow
    """

function = multiply


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()


"""
GPT solution

from typing import List

def multiply(num1: str, num2: str) -> str:
    # Edge case
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    res = [0] * (m + n)

    # Multiply digits (from right to left)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            s = mul + res[p2]

            res[p2] = s % 10
            res[p1] += s // 10

    # Convert to string, skipping leading zeros
    result = []
    for digit in res:
        if not (len(result) == 0 and digit == 0):
            result.append(str(digit))

    return "".join(result)
"""