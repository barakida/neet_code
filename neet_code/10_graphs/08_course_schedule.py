"""
Course Schedule

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:

You are given an array prerequisites where prerequisites[i] = [a, b]
indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
prerequisites[i].length == 2
0 <= a[i], b[i] < numCourses
All prerequisite pairs are unique.
"""

"numCourses = 2, prerequisites = [[0,1]]"
EXAMPLES = [
    {"input": {"numCourses": 2, "prerequisites": [[0, 1]]}, "output": True},
    {"input": {"numCourses": 2, "prerequisites": [[0,1],[1,0]]}, "output": False},
]

COMPLEXITY = """

"""

from collections import deque, defaultdict
from typing import List


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(lambda: {"prerequisite": [], "started": False})
    for a, b in prerequisites:
        graph[a]["prerequisite"].append(b)

    def dsf(course: int) -> bool:
        if not course in graph:
            return True
        if graph[course]["started"]:
            return False
        graph[course]["started"] = True
        for c in graph[course]["prerequisite"]:
            if not dsf(c):
                return False
        del graph[course]
        return True

    for c, _ in prerequisites:
        if not dsf(c):
            return False
    return True


function = can_finish


if __name__ == '__main__':
    import numpy as np

    for e in EXAMPLES:
        print(f"{np.array(e['input']["numCourses"])}")
        print(f"{np.array(e['input']["prerequisites"])}")
        print(function(**e['input']))
        print(f"{np.array(e['output'])}")
        print("\n\n")

    print("\nComplexity:", COMPLEXITY)

