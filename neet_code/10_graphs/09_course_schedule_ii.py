"""
Course Schedule II
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""

from collections import deque
from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    # build graph: b -> a
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    # start with all courses that have no prerequisites
    q = deque([c for c in range(numCourses) if indegree[c] == 0])
    order = []

    while q:
        c = q.popleft()
        order.append(c)
        for nxt in graph[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return order if len(order) == numCourses else []


"""
Complexity
Let:
    V = numCourses
    E = len(prerequisites)
Time: O(V+E)
Space: O(V+E)
"""