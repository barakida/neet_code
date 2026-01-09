"""
Pow(x, n)

def myPow(x: float, n: int) -> float:

Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).
Given a floating-point value x and an integer value n,
implement the myPow(x, n) function, which calculates x raised to the power n.
You may not use any built-in library functions.

Example 1:
Input: x = 2.00000, n = 5
Output: 32.00000

Example 2:
Input: x = 1.10000, n = 10
Output: 2.59374

Example 3:
Input: x = 2.00000, n = -3
Output: 0.12500

Constraints:
-100.0 < x < 100.0
-1000 <= n <= 1000
n is an integer.
If x = 0, then n will be positive.
"""
from neet_code.utils.blueprint import COMPLEXITY

EXAMPLES = [
    {"input": {"x": 2.0, "n": 5}, "output": 32},
    {"input": {"x": 1.1, "n": 10}, "output": 2.59374},
    {"input": {"x": 2.0, "n": -3}, "output": 0.125},
]

# 2**5 = 2 * 2**4 = 2 * 4**2
# 2**7 = 2 * 2**6 = 2 * 4**3 = 2 * 4 * 4**2 = 2 * 4 * 8
# 2**8 = 4**4 = 16**2 = 256

def myPow(x: float, n: int) -> float:

    # edge cases
    if n == 0:
        return 1
    elif x == 0:
        return 0
    elif x == 1:
        return 1

    # init values
    result = 1
    base, n = (x, n) if n > 0 else (1 / x, -n)

    if n < 0:
        base = 1 / base
        n = -n

    while n > 1:
        if n % 2 == 1:
            result *= base
            n -= 1
        else:
            base *= base
            n = n // 2

    return result * base


function = myPow

def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()
