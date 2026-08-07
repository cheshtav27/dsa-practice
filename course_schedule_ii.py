from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return order if len(order) == numCourses else []