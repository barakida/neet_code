"""
Plus One

def plus_one(digits: List[int]) -> List[int]:

You are given an integer array digits, where each digits[i] is the ith digit of a large integer.
It is ordered from most significant to least significant digit, and it will not contain any leading zero.
Return the digits of the given integer after incrementing it by one.

Example 1:
Input: digits = [1,2,3,4]
Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:
Input: digits = [9,9,9]
Output: [1,0,0,0]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List

EXAMPLES = [
    {"input": {"digits": [1,2,3,4]}, "output": [1,2,3,5]},
    {"input": {"digits": [9,9,9]}, "output": [1,0,0,0]},
]

COMPLEXITY = """
Complexity:
time: O(n)
space: O(n)
"""

def plus_one(digits: List[int]) -> List[int]:
    result: List[int] = list()
    keep = 1

    for idx in range(len(digits) - 1, -1, -1):
        val = digits[idx] + keep
        if val < 10:
            keep = 0
        else:
            val = 0
            keep = 1
        result.append(val)
    if keep:
        result.append(1)

    return list(reversed(result))

"""
gpt solution
def plus_one(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
"""


function = plus_one


def main():
    for e in EXAMPLES:
        print(f"input: {e["input"]}")
        print(f"expected: {e['output']}")
        print(f"output: {function(**e["input"])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()


