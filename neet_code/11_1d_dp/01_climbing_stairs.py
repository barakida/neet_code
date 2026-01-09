"""
Climbing Stairs

def climb_stairs(n: int) -> int:

You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""

EXAMPLES = [
    {"input": {"n": 1}, "output": 1},
    {"input": {"n": 2}, "output": 2},
    {"input": {"n": 3}, "output": 3},
]

COMPLEXITY = """

"""


def climb_stairs_1(n: int) -> int:

    visited = dict()

    def dfs(n: int) -> int:

        if n == 0:
            return 1

        count = 0
        if n >= 1:
            count += visited[n - 1] if n in visited else dfs(n - 1)
        if n >= 2:
            count += visited[n - 2] if n in visited else dfs(n - 2)

        visited[n] = count

        return count

    return dfs(n)


def climb_stairs_2(n: int) -> int:

    curr, prev = 1, 0
    for _ in range(n):
        curr, prev= curr + prev, curr

    return curr

function = climb_stairs_2  #  [climb_stairs_1, climb_stairs_2]


def main():
    for e in EXAMPLES:
        print(f"input:\t{e['input']}")
        print(f"output: \t{e['output']}")
        print(f"results:\t{function(**e['input'])}\n\n")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()


"""
0: 0
1: 1
2: 1 + 1, 2
3: 1 + 1 + 1, 2 + 1, 1 + 2
4: 

"""
