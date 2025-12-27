"""
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"target": 10, "position": [1, 4], "speed": [3, 2]}, "output": 1},
    {"input": {"target": 10, "position": [4, 1, 0, 7], "speed": [2, 2, 1, 1]}, "output": 3},
]

COMPLEXITY = """

"""


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pass


function = carFleet


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
